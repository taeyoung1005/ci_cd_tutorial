from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"first": "Hello World!", "second": "Hello World!"}

