"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline
from kedro_tf_multimodal.pipelines.train.pipeline import create_pipeline, create_train_pipeline

# TODO: https://github.com/tensorflow/hub/issues/705
import tensorflow_text as text

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    return {
        "__default__": create_pipeline(), # * Build fusion model
        "train": create_train_pipeline(), # * Train fusion model
        }
