from src.Datascience import logger
from src.Datascience.pipeline.data_ingestionpipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>stage {STAGE_NAME} started <<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx===================x")
except Exception as e:
    logger.exception(e)
    raise e