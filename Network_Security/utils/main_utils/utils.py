import yaml
from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging
import os,sys
import numpy as np
import dill
import pickle

def read_yaml_file(filepath: str) -> dict:
    try:
        with open(filepath,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def write_yaml_file(filepath:str,content:object,replace:bool = False) -> None:
    try:
        if replace:
            if os.path.exists(filepath):
                os.remove(filepath)
        os.makedirs(os.path.dirname(filepath),exist_ok=True)

        with open(filepath,"w") as file:
            yaml.dump(content,file)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def save_numpy_array_data(file_path:str,array:np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            np.save(file_obj,array)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
def save_object(file_path:str,obj:object):
    try:
        logging.info("entered the save_object method of Mainutils class")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
        logging.info("Exited the save_object method of mainutils class")
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
