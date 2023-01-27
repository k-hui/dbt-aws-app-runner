from pydantic import BaseModel
from fastapi import FastAPI


class Model(BaseModel):
    command: str


app = FastAPI()


@app.get('/')
def root():
    return {'message': 'Hello World'}


@app.post('/dbt')
def item(model: Model):
    return {'command': model.command}
