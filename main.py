from iris import Iris
from fastapi import FastAPI
from utils import check_for_models
import numpy as np
from fastapi.responses import RedirectResponse



app = FastAPI()

"""
Adicionando esse redirect só pra facilitar a utilização do endpoint,
qualquer chamada feita na API pelo navegador vai enviar o usuário pro
/docs onde ele poderá inserir os parâmetros pra testar o modelo.
"""
@app.get("/{path:path}")
async def always_redirect_to_docs():
    return RedirectResponse(url="/docs")


"""
Endpoint responsável por receber o input do usuário, enviar o input
para o modelo e retornar qual o tipo de iris os dados apresentados
pelo usuário mais se assemelham.
"""
@app.post("/iris/")
async def classify_iris(iris: Iris):
    iris_type = {
        0:'Iris-setosa',
        1:'Iris-versicolor',
        2:'Iris-virginica',
    }

    data_list = list(iris.dict().values())

    data_array = np.array(data_list).reshape(1, -1)
    
    model = check_for_models()

    result = model.predict(data_array)[0]


    return {'result':iris_type[result]}




