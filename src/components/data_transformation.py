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

@dataclass
class DataTransformationConfig:
    # we need to create a path to help us save any model into a pickle file
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns=['SeniorCitizen','tenure','MonthlyCharges','TotalCharges']
            categorical_columns=['gender','Partner', 'Dependents', 'PhoneService','PaperlessBilling',
                                  'MultipleLines','InternetService', 'OnlineSecurity', 'OnlineBackup',
                'DeviceProtection', 'TechSupport', 'StreamingTV','Churn',
                'StreamingMovies', 'Contract', 'PaymentMethod',
            ]

            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())
                ]
            )

            cat_pipeline=Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler())
                ]
            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns)
                ("cat_pipeline",cat_pipeline,categorical_columns)   
                ]
            )

            return preprocessor
   
        except Exception as e:
            raise CustomException(e,sys)  
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv()
            test_df=pd.read_csv()

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()
        except:
            pass