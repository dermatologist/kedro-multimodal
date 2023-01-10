
```
saved_model_cli show --all --dir data/07_model_output/train/
saved_model_cli show --all --dir data/08_reporting/
```


MetaGraphDef with tag-set: 'serve' contains the following SignatureDefs:

signature_def['__saved_model_init_op']:
  The given SavedModel SignatureDef contains the following input(s):
  The given SavedModel SignatureDef contains the following output(s):
    outputs['__saved_model_init_op'] tensor_info:
        dtype: DT_INVALID
        shape: unknown_rank
        name: NoOp
  Method name is:

signature_def['serving_default']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['age'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 1)
        name: serving_default_age:0
    inputs['bp'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 1)
        name: serving_default_bp:0
    inputs['gender'] tensor_info:
        dtype: DT_STRING
        shape: (-1, 1)
        name: serving_default_gender:0
    inputs['input_1'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 224, 224, 3)
        name: serving_default_input_1:0
    inputs['text_input_for_bert'] tensor_info:
        dtype: DT_STRING
        shape: (-1)
        name: serving_default_text_input_for_bert:0
    inputs['zip'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 1)
        name: serving_default_zip:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['fusion_1'] tensor_info:
        dtype: DT_FLOAT
        shape: (-1, 1)
        name: StatefulPartitionedCall_2:0
  Method name is: tensorflow/serving/predict