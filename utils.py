import os
import joblib
from pipeline import run_pipeline

#Verificação se já existe algum modelo
def check_for_models():
    """
    Essa validação não é pensando muito no ciclo de vida do modelo em si
    é mais uma facilitação pra evitar lotar a máquina.
    """
    files = os.listdir('.')
    
    pkl_files = [file for file in files if file.endswith('.pkl')]
    
    #Se já existir 1 best model, usá-lo
    if len(pkl_files)==1:
        return joblib.load(pkl_files[0])
    #Caso não exista nenhum modelo, treinar um novo
    elif len(pkl_files)<1:
        model_name = run_pipeline()
        return joblib.load(model_name)
    #Caso esteja lotado, deletar todos e rodar o melhor
    else:
        delete_models()
        model_name = run_pipeline()
        return joblib.load(model_name)        

#Deleção dos modelos existentes
def delete_models():
    files = os.listdir('.')
    
    pkl_files = [os.remove(file) for file in files if file.endswith('.pkl')]
    
    if pkl_files:
        return True
    else:
        return False