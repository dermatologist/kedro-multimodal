import json
import cv2
import requests
import base64
import numpy as np

def main():



    # Load an image from file
    im = cv2.imread("data/01_raw/imageset/img1.jpg")

    # Base64 encode it
    # (you can also load the raw png data from file using open instead of opencv)
    encoded = base64.b64encode(cv2.imencode(".jpg", im)[1].tobytes())

    json_data = {
        "signature_name": "serving_bytes",
        "instances": [{
            "age": 24,
            "bp": 85,
            "gender": "Male",
            "zip": 12345,
            "text_input_for_bert": "This is a test sentence.",
            "input_bytes": {"b64": encoded.decode("utf-8")}
        }]
    }

    _json_data = {
        "signature_name": "serving_default",
        "instances": [{
            "age": 24,
            "bp": 85,
            "gender": "Male",
            "zip": 12345,
            "text_input_for_bert": "This is a test sentence.",
            "input_1": np.asarray(im).tolist()
        }]
    }

    print(_json_data)

    # Wrap it in json (tf-serving compatible with instances and b64)
    data = json.dumps(json_data)

    # Standard port for tf-serving rest interface is 8501
    # Request Format: http://domain:[tf-serving-port]/v1/models/[model_name]:predict
    resp = requests.post("http://localhost:8501/v1/models/train:predict", data)

    # Load base 64 encoded image string from response
    print(resp.json())


if __name__ == "__main__":
  main()
