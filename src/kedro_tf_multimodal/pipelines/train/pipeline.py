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


bert_model = modular_pipeline(pipe=download_bert, parameters={"params:bert_model": "params:fusion"})
tabular_model = modular_pipeline(pipe=tabular_model_pipeline, outputs={"tabular_model": "tabular_model_saved"}, parameters={
                              "params:tabular": "params:fusion"})


inputs = {"parameters": "params:fusion", "bert_model": "bert_model_saved", "tabular_model": "tabular_model_saved",
          "image_model": "chexnet_weights"}
_fusion_pipeline = create_fusion_pipeline(**inputs)
fusion_model = modular_pipeline(pipe=_fusion_pipeline, outputs={
                                "fusion_model": "fusion_model"})

def create_pipeline(**kwargs) -> Pipeline:
    return bert_model + tabular_model + fusion_model

