from Network_Security.components.data_ingestion import DataIngestion
from Network_Security.components.data_validation import DataValidation
from Network_Security.components.data_transformation import DataTransformation
from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging
import sys
from Network_Security.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from Network_Security.entity.config_entity import TrainingPipelineConfig
if __name__ =="__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate Data ingestion")
        dataingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestion_artifact)

        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestion_artifact,data_validation_config)
        logging.info("Initiate Data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)


        logging.info("Data Transformation Started")
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()

        print(data_transformation_artifact)

        logging.info("Data Transformation Completed")
        

    except Exception as e:
        raise NetworkSecurityException(e,sys)
