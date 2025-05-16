from prefect import flow, task
from datetime import datetime
import pandas as pd 

import os
import sys

import shutil

# Function preprocess data requirements: 
    # 1. Read csv file
    # 2. remove any missing values 
    # 3. feature engineering (create new colums)

#Preprocess data 
@task
def preprocess_data(): 
    # Load raw data 
    df = pd.read_csv("Datasets/AIML Dataset.csv")

    # remove missing values & irrelevant columns   
    df_model = df.drop(["step", "nameOrig", "nameDest", "isFlaggedFraud"], axis = 1)
    
    # feature engineering 
    df_model.head()

    # Save and copy our preprocesses Dataset to our Model file 
    # First - Save to csv file 
    df_model_csv = df_model.to_csv("AIMLDataset.csv") 
    
    return df_model

# Load Data 
@task
def load_data(df: pd.DataFrame): 
    print("Loading preprocessed data...\n")
    print(df)

# @task
# def mlflow_environment(experiment_name):
#     mlflow.set_tracking_uri("http://127.0.0.1:5000")
#     mlflow.set_experiment(experiment_name)
#     experiment = mlflow.get_experiment_by_name(experiment_name)

#     return experiment.experiment_id
#Defining the flow 
@flow(log_prints=True)
def etl():
    raw_data = preprocess_data()
    load_data(raw_data)

if __name__ == "__main__":
    etl()
