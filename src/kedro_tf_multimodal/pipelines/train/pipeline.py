"""
This is a boilerplate pipeline 'train'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline

from kedro_tf_utils.pipelines.train.pipeline import create_train_pipeline
from kedro_tf_utils.pipelines.fusion.pipeline import create_fusion_pipeline
from kedro.pipeline.modular_pipeline import pipeline as modular_pipeline
from kedro_tf_text.pipelines.bert.pipeline import download_bert

from kedro_tf_text.pipelines.tabular.pipeline import tabular_model_pipeline
from kedro_tf_image.pipelines.preprocess.pipeline import create_classification_layer

from kedro_tf_text.pipelines.preprocess.pipeline import process_text_pipeline, glove_embedding
from kedro_tf_text.pipelines.cnn.pipeline import cnn_text_pipeline

# Download BERT model and save it in the TF Hub format in bert_model_saved catalog
bert_model = modular_pipeline(pipe=download_bert, parameters={
                              "params:bert_model": "params:multimodal"})
# creates a tabular model from the tabular data and saves it in the tabular_model_saved catalog.
# The tabular data in csv has ID, column1, column2, columnx, label format: Refer to https://github.com/dermatologist/kedro-tf-text
tabular_model = modular_pipeline(pipe=tabular_model_pipeline, outputs={"tabular_model": "tabular_model_saved"}, parameters={
    "params:tabular": "params:multimodal"})

""" For CNN TEXT MODEL"""
preprocess_text_pipeline = modular_pipeline(pipe=process_text_pipeline, parameters={"params:embedding": "params:multimodal"})
preprocess_glove_embedding = modular_pipeline(pipe=glove_embedding, parameters={"params:embedding": "params:multimodal"})
# save word2vec_embedding from above step (include in catalogue). This is needed for preprocessing text data for CNN model
cnn_text_pipeline = modular_pipeline(pipe=cnn_text_pipeline, parameters={"params:cnn_text_model": "params:multimodal"})
cnn_text_final = preprocess_glove_embedding + cnn_text_pipeline

# Loads the chexnet weights and adds a classification layer to it.
chexnet_model_pipeline = create_classification_layer()
chexnet_model = modular_pipeline(pipe=chexnet_model_pipeline, parameters={
                                 "params:add_layer": "params:multimodal"})  # chexnet_weights -> chexnet_model

# Creates a fusion model from the bert, tabular and image models and saves it in the fusion_model catalog.
# model names should start with model type (bert, tabular, image or text)
""" BERT
inputs = {"parameters": "params:multimodal", "bert_model": "bert_model_saved", "tabular_model": "tabular_model_saved",
          "image_model": "chexnet_model"}
"""

""" CNN TEXT MODEL"""
inputs = {"parameters": "params:multimodal", "text_model": "cnn_text_model", "tabular_model": "tabular_model_saved",
          "image_model": "chexnet_model"}

_fusion_pipeline = create_fusion_pipeline(**inputs)
fusion_model = modular_pipeline(pipe=_fusion_pipeline, outputs={
                                "fusion_model": "fusion_model"})

# ! COPY vocab.txt from bert_model_saved to fusion_model, if using BERT

# Trains the fusion model and saves it in the trained_model catalog.
# * Replace "processed_data": "processed_text", "text_data": "text_data", WITH "bert_data": "text_data", if using BERT
train = {"parameters": "params:multimodal", "model": "fusion_model", "outputs": "trained_model",
         "processed_data": "processed_text", "text_data": "text_data", "tabular_data": "tabular_data", "image_data": "image_data"}

train_pipeline = create_train_pipeline(**train)


# * Build fusion model
def create_pipeline(**kwargs) -> Pipeline:
    ## bert_model can replace cnn_text_final
    return cnn_text_final + tabular_model + chexnet_model + fusion_model

# * Train fusion model
def create_train_pipeline(**kwargs) -> Pipeline:
    # preprocess_text_pipeline not needed for BERT
    return preprocess_text_pipeline + train_pipeline