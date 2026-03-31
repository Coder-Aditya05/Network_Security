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
Data Validation Contsant start with Data_VAlidation var name 
"""

DATA_VALIDATION_DIR_NAME : str = "data_validation"
DATA_VALIDATION_VALID_DIR : str = "validated"
DATA_VALIDATION_INVALID_DIR : str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR : str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME : str = "report.yaml"