import os
import sys
import numpy as np
import pandas as pd


"""
defining common constant variable for training pipeline
"""

TARGET_COLUMN = "Result"
PIPELINE_NAME:str = "Network_Security"
ARTIFACT_DIR : str = "Artifacts"
FILE_NAME : str = "phisingData.csv"
TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str="test.csv" 

SCHEMA_FILE_PATH  = os.path.join("data_schema","schema.yaml")

SAVE_MODEL_DIR = os.path.join("saved_models")
"""
Data Ingestion Constant start with Data_ingestion var name
"""

DATA_INGESTION_COLLECTION_NAME : str = "Network_Data"
DATA_INGESTION_DATABASE_NAME:str = "ADITYA_AI"
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR : str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTED_TRAIN_TEST_SPLIT_RATION: float=0.2


"""
Data Validation Contsant start with Data_Validation var name 
"""

DATA_VALIDATION_DIR_NAME : str = "data_validation"
DATA_VALIDATION_VALID_DIR : str = "validated"
DATA_VALIDATION_INVALID_DIR : str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR : str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME : str = "report.yaml"

"""
Data Transformation Constant start with Data_Transformation var name 
"""

DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR : str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR : str = "transformed_object"

## KNN IMPUTER CLASS TO REPLACE NAN VALUES
DATA_TRANSFORMATION_IMPUTER_PARAMS : dict = {
    "missing_values" : np.nan,
    "n_neighbors":3,
    "weights":"uniform",
}

PREPROCESSING_OBJECT_FILE_NAME ="prprocessing.pkl"


"""
Model Trainer Constant start with Model_trainer var name
"""

MODEL_TRAINER_DIR_NAME : str = "Model_trainer"
MODEL_TRAINER_TRAINED_DIR : str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME :str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE : float = 0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD : float = 0.05