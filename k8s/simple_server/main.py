import socket
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "/hello"

@app.get("/hello")
def hello():
    ret = "You hit : " + socket.gethostname()
    return ret