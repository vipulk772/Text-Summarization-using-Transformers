from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

'''STAGE_NAME= "Data Ingestion Stage"
try:
    logger.info(f" stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f" stage {STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Data Validation Stage"
try:
    logger.info(f" stage {STAGE_NAME} started")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f" stage {STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME= "Data Transformation Stage"
try:
    logger.info(f" stage {STAGE_NAME} started")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f" stage {STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME= "Model Training Stage"
try:
    logger.info(f" stage {STAGE_NAME} started")
    data_ingestion = ModelTrainerTrainingPipeline()
    data_ingestion.main()
    logger.info(f" stage {STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e'''


STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e