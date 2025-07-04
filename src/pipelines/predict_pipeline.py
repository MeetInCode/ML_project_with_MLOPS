import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        # This block of code is responsible for making predictions using a trained machine learning model.
        try:
            # Define the file paths for the saved model and preprocessor objects.
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            
            print("Before Loading")
            
            # Load the trained model and preprocessor from their respective files.
            preprocessor = load_object(file_path=preprocessor_path)
            model = load_object(file_path=model_path)
            
            
            # Print a message after loading the objects (for debugging purposes).
            print("After Loading")
            
            # Use the preprocessor to transform the input features (e.g., scaling, encoding).
            data_scaled = preprocessor.transform(features)
            
            # Use the loaded model to make predictions on the processed features.
            preds = model.predict(data_scaled)
            
            # Return the predictions.
            return preds
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
