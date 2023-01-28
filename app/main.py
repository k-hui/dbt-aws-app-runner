import asyncio
import inspect
from pydantic import BaseModel
from fastapi import FastAPI


def log(message: str):
    func = inspect.stack()[1].function
    print(f'[dbt]::{func}::{message}')


class DbtModel(BaseModel):
    cmd: str


async def dbt_cmd(model: DbtModel):
    c = model.cmd

    if not c.startswith('dbt'):
        message = f"Command: '{c}' is not a valid dbt command."
        log(f'message={message}')
        return {'message': message, 'code': 400}

    log(f'Running=<{c}>')
    process = await asyncio.create_subprocess_shell(c)
    await process.wait()

    if process.returncode != 0:
        message = f"Command: <{c}> failed with return code {process.returncode}."
        log(f'message={message}')
        return {'message': message, 'code': 500}

    message = f"Command: <{c}> ran successfully."
    log(f'message={message}')
    return {'message': message, 'code': 200}


app = FastAPI()


@app.get('/')
def root():
    return {'message': 'Hello World'}


@app.post("/dbt")
async def dbt(item: DbtModel):
    return await dbt_cmd(item)
