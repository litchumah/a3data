from iris import Iris
from fastapi import FastAPI
from utils import check_for_models
import numpy as np
from fastapi.responses import RedirectResponse



app = FastAPI()

@app.get("/{path:path}")
async def always_redirect_to_docs():
    return RedirectResponse(url="/docs")

@app.post("/iris/")
async def classify_iris(iris: Iris):
    iris_type = {
        0:'Iris-setosa',
        1:'Iris-versicolor',
        2:'Iris-virginica',
    }

    model = check_for_models()

    data_list = list(iris.dict().values())

    data_array = np.array(data_list)

    if model:
        result = model.predict(data_array.reshape(1, -1))[0]
    
    return {'result':iris_type[result]}




