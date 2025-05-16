# Using the Requirements for analysing how each approach has went so far 

## Requirements for Fraud detection & MLOPS Pipline: 
    ```
        **FILE STRUCTURE**: 

        ML Projects/
            -> MLOPS Pipeline 
                -> Preprocessing/
                    -> Preprocessing.py
                    -> Datasets/
                        -> AIML Dataset.csv
                -> Models/
                    -> LogisticRegression.py [X]
                    -> LinearRegression.py
                    -> RNN.py
                -> Monitoring/
                    TBC
                -> Feedback & Iteration/
                    TBC



    
        1 - Create data ingest and preprocess step. 
            1.1 - this will include feature engineering & removing missing values [X]
            1.2 - Revised using Apache Airflow due to issues with imports. Prefect was then used instead. [X]
            1.3 - Research Apache Kafka which can gather real-time data from [TBD]
            
        2 - Model Training & Validation 
            2.1 - Experiment Tracking: Tools like MLflow or DVC help track experiments, hyperparameters, and metrics.
            2.2 - Version Control: Maintain versioning for datasets, code and models using GIT or specialized tools like DVC
            2.3 - Cross-Validation: Use techniques like k-fold cross-validation to asses model robustness
            2.4 - Automated retraining: Schedule periodic retraining to keep models up-to-date with new data

        3 - Model Deployment 
            3.1 - Containerization: Use Docker to package the model & its dependenices into a potable container 
            3.2 - Orchestration: Kubernetes can manage containerized deployments at scale 
            3.3 - API Endpoints: Expose models as RESTful APIs using frameworks like FastAPI or Flask
            3.4 - CI/CD Integration: Integrate depliyment workflows with CI/CD piplines using Jenkins, GitHub Actions or GitLab CI

        4 - Model monitioring & Maintenance
            4.1 - Performance Metrics: Track metrics like accuracy, precision, recall & F1-Score
            4.2 - Data Drift Detection: Monitor changes in input data distributions using tools like Evidently AI or WhyLabs
            4.3 - Logging & Alerts: Implement logging mechanisms and set up alerts for anomalies 
            4.4 - Scalability: Ensure the infrastructure can handle varying workloads without compromising performance 

        5 - Feedback & interation 
            5.1 - A/B testing: Compare different version of a model to determine which performs better
            5.2 - User feedback: Incorporate feedback from end-users to enhance model usability 
            5.3 - Continuous Improvement: Use insights gained from monitioring & feedback to update & retrain models. 
    ```