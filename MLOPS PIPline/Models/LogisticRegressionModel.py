from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import pandas as pd 

import os
import sys

df = pd.read_csv("AIMLDataset.csv")
df_model = df
categorical = ["type"]
numeric = ["amount", "oldbalanceOrg", "newbalanceOrig", "oldbalanceDest", "newbalanceDest"]

y = df_model["isFraud"]
X = df_model.drop("isFraud", axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

preprocessor = ColumnTransformer (
    transformers= [
        ("num", StandardScaler(), numeric),
        ("cat", OneHotEncoder(drop="first"), categorical)
    ],
    remainder="drop"
)

# Setup our pipeline 
print("\nCreating Pipeline......\n")
pipeline = Pipeline([
    ("prep", preprocessor), 
    ("clf", LogisticRegression(class_weight="balanced", max_iter=1000))
])
print("\nFitting Pipeline......\n")
# fit our data to the pipeline
pipeline.fit(X_train, y_train)

print("\nPredicting Values......\n")
# Predict values
y_pred = pipeline.predict(X_test)

# Print out our classification report 
print("\n************************ CLASSIFICATION REPORT ************************\n", classification_report(y_test, y_pred))
print("\n************************ PIPELINE SCORE ************************\n",  round(pipeline.score(X_test, y_test) * 100, 1))

# Add a check to see if Pipline score is reliable enough for deployment
if round(pipeline.score(X_test, y_test) * 100, 1) > 90: 
    # Save our model 
    import pickle 
    with open("fraud_pipeline.pickle", "wb") as f: 
        pickle.dump(pipeline,  f)
    
    print("\nPipeline Created!\n")
else: 
    print("\nPipeline Not Created! Check Classification Report & Pipeline score for model performance\n")


