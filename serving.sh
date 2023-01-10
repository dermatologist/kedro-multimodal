# Download the TensorFlow Serving Docker image and repo
docker pull tensorflow/serving

# Location of  models
TESTDATA="$(pwd)/data/08_reporting/train"

echo $TESTDATA
# Start TensorFlow Serving container and open the REST API port
docker run -t --rm -p 8501:8501 \
    -v "$TESTDATA:/models/train/1" \
    -e MODEL_NAME=train \
    tensorflow/serving &

# Query the model using the predict API
# curl -d '{"instances": [1.0, 2.0, 5.0]}' \
#     -X POST http://localhost:8501/v1/models/half_plus_two:predict
