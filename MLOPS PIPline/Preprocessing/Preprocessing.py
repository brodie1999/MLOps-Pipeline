# Using Prefect which can handle large amounts of data and utilises DAG (Directed Acyclic Graphs)
from prefect import task, flow
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
    # Using shutil to copy our file to our Model folder
    shutil.copy("AIMLDataset.csv", "../Models/")
    
    
    return df_model

# Load Data 
@task
def load_data(df: pd.DataFrame): 
    print("Loading preprocessed data...\n")
    print(df)
    
#Defining the flow 
@flow(log_prints=True)
def etl():
    raw_data = preprocess_data()
    load_data(raw_data)

if __name__ == "__main__":
    etl()