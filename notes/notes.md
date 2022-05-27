[<KerasTensor: shape=(None, 2) dtype=float32 (created by layer 'input_categorical_vars_all')>, <KerasTensor: shape=(None, 1) dtype=float32 (created by layer 'input_continuous_all')>, <KerasTensor: shape=(None, 224, 224, 3) dtype=float32 (created by layer 'input_1')>]


[<KerasTensor: shape=(None, 3) dtype=float32 (created by layer 'normalization')>]
[<KerasTensor: shape=(None, 2) dtype=float32 (created by layer 'input_categorical_vars_all')>, <KerasTensor: shape=(None, 1) dtype=float32 (created by layer 'input_continuous_all')>, <KerasTensor: shape=(None, 224, 224, 3) dtype=float32 (created by layer 'input_1')>]


<KerasTensor: shape=(None, 1) dtype=float32 (created by layer 'age')>, <KerasTensor: shape=(None, 1) dtype=float32 (created by layer 'bp')>, <KerasTensor: shape=(None, 1) dtype=string (created by layer 'gender')>, <KerasTensor: shape=(None, 1) dtype=float32 (created by layer 'zip')>, <KerasTensor: shape=(None, 224, 224, 3) dtype=float32 (created by layer 'input_1')>





    # imgs = tf.convert_to_tensor(_imgs, dtype=tf.float32)

    # tabular = tf.convert_to_tensor(preprocessed_inputs, dtype=tf.float32)
    # print(preprocessed_inputs_cat)
    # x = tf.concat([csv_features_dict, imgs], axis=1)
    # print([csv_features_dict, _imgs])

    # print(multi_modal.summary)

    # print(np.shape(_imgs))
    # print(np.shape(csv_features_dict))
    # dataset = tf.data.Dataset.from_tensor_slices(csv_features_dict)
    # print(multi_modal.inputs)
    # print(inputs)
    # print(categorical_inputs)
    # print(numeric_inputs)
    print(multi_modal.inputs)







    # for name, value in csv_features_dict.items():
    #     print(name, value.shape)


    # Split the dataset for text
    # X_train, X_test, y_train, y_test = train_test_split(
    #     text_dataset, y, test_size=0.2, random_state=42)