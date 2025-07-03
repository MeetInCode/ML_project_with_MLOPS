import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

# This dataclass defines the configuration for the data transformation process.
# It contains the file path where the preprocessor object (such as a fitted sklearn pipeline) will be saved after training, so it can be reused later for transforming new data.
@dataclass
class DataTransformationConfig:
    # Path to save the serialized preprocessor object (e.g., a pickle file)
    preprocessor_obj_file_path = os.path.join('artifacts', "proprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),  # handling the missing values in numerical columns
                ("scaler",StandardScaler())  # scaling the numerical columns

                ]
            )

            cat_pipeline=Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),  # handling the missing values in categorical              
                ("one_hot_encoder",OneHotEncoder()),  # encoding the categorical columns
                ("scaler",StandardScaler(with_mean=False))  # scaling the numerical columns

                ]

            )

            logging.info("Categorical columns encoding completed successfully")
            logging.info("Numerical columns scaling completed successfully")


            # ColumnTransformer is used to apply different transformations to different columns of the DataFrame.
            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)

                ]


            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        




    def initiate_data_transformation(self,train_path,test_path):

        try:
            # Read the training and test data from the specified paths
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")




            # Explanation of the data transformation process:

            # 1.
            logging.info("Obtaining preprocessing object")

            # 2. Get the preprocessing object, which is a scikit-learn ColumnTransformer
            # that applies the necessary transformations (imputation, encoding, scaling) to the appropriate columns.
            preprocessing_obj = self.get_data_transformer_object()

            # 3. Define the target column and the numerical columns.
            #    "math_score" is the target variable we want to predict.
            #    "writing_score" and "reading_score" are the numerical features.
            target_column_name = "math_score"
            numerical_columns = ["writing_score", "reading_score"]

            # 4. Split the training dataframe into input features (X) and target (y).
            #    Drop the target column from the features.
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            # 5. Do the same split for the test dataframe.
            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            # 6. Log that we are applying the preprocessing object to the data.
            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            # 7. Fit the preprocessing object on the training features and transform them.
            #    Also, transform the test features (without fitting).
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            # 8. Concatenate the transformed features and the target values for both train and test sets.
            #    np.c_ stacks the arrays column-wise, so the last column will be the target.
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                # This returns the file path where the preprocessor (scikit-learn transformer) object is saved.
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)