import os
import sys
from src.exception import CustomException
from src.logger import logging


import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig    

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer




# The DataIngestionConfig dataclass is used to define and manage the file paths for the data files involved in the ingestion process.
# It specifies default locations for the training data, test data, and the raw (original) data, all of which will be stored in an 'artifacts' directory.
# This configuration makes it easy to reference and update these paths throughout the data ingestion workflow.

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")  # Path where the training set will be saved
    test_data_path: str = os.path.join('artifacts', "test.csv")    # Path where the test set will be saved
    raw_data_path: str = os.path.join('artifacts', "data.csv")     # Path where the raw/original data will be saved



class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            # Create the directory for storing the train, test, and raw data CSV files if it doesn't already exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) 

            # Save the original dataframe as a raw data CSV file for reference or backup
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            # Save the training set to a CSV file at the path specified in the ingestion config.
            # The file will not include the DataFrame index and will include the header row.
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
        
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return(
                # Return the paths to the train and test data CSV files
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
   
    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
   


