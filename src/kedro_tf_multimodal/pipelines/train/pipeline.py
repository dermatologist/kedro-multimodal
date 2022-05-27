"""
This is a boilerplate pipeline 'train'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline

from kedro_tf_multimodal.pipelines.train.nodes import train_multimodal


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([])


def create_train_pipeline(datasets={}, **kwargs) -> Pipeline:
    return pipeline([

                    node(
                        train_multimodal,
                        [datasets.get("tabular_data", "tabular_data"),
                         datasets.get("image_data", "image_data"),
                         datasets.get("fusion_model", "fusion_model"),
                         datasets.get("parameters", "parameters")],
                        datasets.get("trained_model", "trained_model"),
                        name="train_model"
                    ),
                    ])
