import os
import joblib

def check_for_models():
    files = os.listdir('.')
    
    pkl_files = [file for file in files if file.endswith('.pkl')]
    
    if pkl_files:
        return joblib.load(pkl_files[0])
    else:
        return False


def delete_models():
    files = os.listdir('.')
    
    pkl_files = [os.remove(file) for file in files if file.endswith('.pkl')]
    
    if pkl_files:
        return True
    else:
        return False