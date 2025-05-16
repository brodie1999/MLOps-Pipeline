import os
import warnings
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import sklearn

import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature

# Track server uri for logging 
mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")
mlflow.set_experiment("Logistic Regression Model - Fraud")

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score, mean_squared_error, mean_absolute_error, r2_score, accuracy_score
from sklearn.linear_model import LogisticRegression

import logging

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# # Using MLflow we can keep track of experiements, log parameters & store models. 
# Set the experiment id 
mlflow.set_experiment(experiment_id="0")
mlflow.autolog()

# Evaluation Metrics 
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    accuracy = accuracy_score(actual, pred)
    return rmse, mae, r2, accuracy

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Read csv file
    
    df = pd.read_csv("AIMLDataset.csv")
    df_model = df
        
    y = df_model["isFraud"]
    X = df_model.drop("isFraud", axis=1)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

    # Start MLflow experiment
    with mlflow.start_run():

        categorical = ["type"]
        numeric = ["amount", "oldbalanceOrg", "newbalanceOrig", "oldbalanceDest", "newbalanceDest"]

        preprocessor = ColumnTransformer(
            transformers = [
                ("num", StandardScaler(), numeric),
                ("cat", OneHotEncoder(drop="first"), categorical)
            ],
        )
        
        pipeline = Pipeline([
            ("prep", preprocessor), 
            ("clf", LogisticRegression(class_weight="balanced", max_iter=1000))
        ])
        
        # Fit on training data 
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)

        # Get metrics
        (rmse, mae, r2, accuracy) = eval_metrics(y_test, y_pred)

        # Log parameters & metrics
        print("\n RMSE: %s\n" % rmse)
        print("\n MAE: %s\n" % mae)
        print("\n R2: %s\n" % r2)
        print("\n Accuracy: %s\n" % (accuracy * 100))        
        
        mlflow.log_param("rmse", rmse)
        mlflow.log_param("mae", mae)
        mlflow.log_param("r2", r2)
        mlflow.log_metric("accuracy", accuracy)

        # Set a tag that we can use to remind ourselves what this run was for 
        mlflow.set_tag("Training info", "Basic LR (Logistic Regression) Model for fraudulent Back Transactions")
        # Infer the model signature
        signature = infer_signature(X_train, pipeline.predict(X_train))

        # Log model
        # pipeline = mlflow.pyfunc.load_model("runs:/<run_id>/model")
        model_info = mlflow.sklearn.log_model(
            sk_model = pipeline, 
            artifact_path="fraud_model", 
            signature=signature, 
            input_example=X_train, 
            registered_model_name="fraud-detection",
        )

        
        



