"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from kedro_tf_utils.pipelines import fusion
from kedro_tf_multimodal.pipelines.train.pipeline import create_train_pipeline
def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    catalog = dict()

    return {
        "__default__": fusion.pipeline.create_fusion_pipeline(catalog) + create_train_pipeline(catalog),
        "train": create_train_pipeline(catalog)

        }
