import requests
import json
import base64
import numpy as np

MODEL_NAME = "stage-1"
MODEL_VERSION = 1
host_port = "http://localhost:8000"
live_path = "/v2/health/live"
health_path = "/v2/health/ready"
model_ready_path = f"/v2/models/{MODEL_NAME}/versions/{MODEL_VERSION}/ready"
server_meta_path = f"/v2/models/{MODEL_NAME}/versions/{MODEL_VERSION}"
infer_path = f"/v2/models/{MODEL_NAME}/versions/{MODEL_VERSION}/infer"


def is_ok(func):
    def func_with_ok(*args, **kwargs):
        response = func(*args, **kwargs)
        if response.status_code == 200:
            print(f"{func.__name__}: OK")
        else:
            print(f"{func.__name__}: Error")
        print(response.text)
        return response
    return func_with_ok


@is_ok
def live():
    return requests.get(host_port + live_path)


@is_ok
def health():
    return requests.get(host_port + health_path)


@is_ok
def model_ready():
    return requests.get(host_port + model_ready_path)


def get_server_meta(server_name: str) -> None:
    response = requests.get(host_port + server_meta_path)
    if response.status_code == 200:
        print("get_server_meta: OK")
    else:
        print("get_server_meta: Error")
    json_str = json.dumps(response.json(), indent=4)
    with open(f"./{server_name}_server_meta.json", "w") as json_file:
        json_file.write(json_str)
    return


def infer1():
    input_data = "tangjicheng"
    input_data = input_data.encode("utf-8")
    input_data = np.array([input_data], np.object_)
    input_data = input_data.tobytes()

    data = {
        "id": "123",
        "parameters": {"a": 1},
        "inputs": [{"name": "input_str", "shape": [1], "datatype":"BYTES", "data": [input_data]}, ],
        "outputs": [{"name": "output_str", "shape": [1], "datatype":"BYTES"}, ]
    }
    print(str(data))

    response = requests.post(host_port + infer_path, json=str(data))
    if response.status_code == 200:
        print("infer: OK")
    else:
        print("infer: Error")
        print(response.status_code, response.text,
              response.content, response.headers)

def test(model_name:str):
    global MODEL_NAME
    global model_ready_path
    global server_meta_path
    global infer_path

    MODEL_NAME = model_name
    MODEL_VERSION = 1
    model_ready_path = f"/v2/models/{MODEL_NAME}/versions/{MODEL_VERSION}/ready"
    server_meta_path = f"/v2/models/{MODEL_NAME}/versions/{MODEL_VERSION}"
    infer_path = f"/v2/models/{MODEL_NAME}/versions/{MODEL_VERSION}/infer"

    live()
    health()
    model_ready()
    
    get_server_meta(model_name)
    
    infer1()

if __name__ == "__main__":
    test("stage-1")
