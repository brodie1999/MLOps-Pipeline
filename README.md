# Machine Learning OPS Pipline
This project will look at developing an MLOPS pipline for fraud detection. 

## Aims & Objectives 

    The aim of this project is to:
        -> Further understand Machine Learing
        -> Understand how Machine Learning Piplines are built.
        -> Gain insight into how to deploy and manage ML models
        -> Set out a set of requirements and goals such as what business problems am I trying to solve?
        -> Collect data based on the business problems
        -> Conduct Model development and Training
        -> Version Control & Reproducibility
        -> Deployment & Infrastructure
        -> Continuous Integration & Delivery
        -> Monitoring & Performance Tracking
        -> Continuous Learning & Model Updates
        -> Security & Governance 

## **Requirements**

Q: What business Problems to solve: 
    -> Fraud Detection 

### Requirements for Fraud detection & MLOPS Pipline: 

        1 - Create data ingest and preprocess step 
            1.1 - this will include feature engineering & removing missing values
            1.2 - Using Apache Airflow to handle large amounts of data. Airflow uses DAG (Directed Acyclic Graphs). 
                   (REQ 1.2: This has been changed to Prefect for now)
            1.3 - Research Apache Kafka which can gather real-time data from 
            
        2 - Model Training & Validation (MLflow & Logistic Regression)
            2.1 - Experiment Tracking: Tools like MLflow or DVC help track experiments, hyperparameters, and metrics.
            2.2 - Version Control: Maintain versioning for datasets, code and models using GIT or specialized tools like DVC
            2.3 - Cross-Validation: Use techniques like k-fold cross-validation to asses model robustness
            2.4 - Automated retraining: Schedule periodic retraining to keep models up-to-date with new data

        3 - Model Deployment (Flask API, Docker & Kubernetes)
            3.1 - Containerization: Use Docker to package the model & its dependenices into a potable container 
            3.2 - Orchestration: Kubernetes can manage containerized deployments at scale 
            3.3 - API Endpoints: Expose models as RESTful APIs using frameworks like FastAPI or Flask
            3.4 - CI/CD Integration: Integrate depliyment workflows with CI/CD piplines using Jenkins, GitHub Actions or GitLab CI

        4 - Model monitioring & Maintenance (MLflow)
            4.1 - Performance Metrics: Track metrics like accuracy, precision, recall & F1-Score
            4.2 - Data Drift Detection: Monitor changes in input data distributions using tools like Evidently AI or WhyLabs
            4.3 - Logging & Alerts: Implement logging mechanisms and set up alerts for anomalies 
            4.4 - Scalability: Ensure the infrastructure can handle varying workloads without compromising performance 

        5 - Feedback & interation (TBD)
            5.1 - A/B testing: Compare different version of a model to determine which performs better
            5.2 - User feedback: Incorporate feedback from end-users to enhance model usability 
            5.3 - Continuous Improvement: Use insights gained from monitioring & feedback to update & retrain models. 

## About Machine Learning Operations 

    source: Google Cloud -> https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning

    By using the above document and following a guide to help keep us on the right track, I will aim to build an MLOPS Pipline for fraud detection.
    Notes will be produced when conducting this project.

    A Machine learning pipline refers to the complete workflow and processes of building and deploying a machine learning model.

    It automates and standardizes the workflow involved in creating a machine learning model.

    A machine learning pipline consists of sequential steps:

        -> Data extraction
        -> Preprocessing
        -> Model training
        -> Deployment

    It is a central production for data science teams, incorporating best practices and enabling scalable execution.
    They are great if you are managing multiple models or just updating a single model, an end-to-end machine learning pipline is essential for effective
    and efficient implementation.

## Benefits of an End-to-End ML Pipline 

    The benefits are:

        -> Ensure reproducibility: By executing the pipline multiple times with the same inputs, we achieve consistent outputs, which enhances the reproducibility
                                        reliability of machine learning models
        -> Simplify Workflow: The pipline automates multiple steps in the machine learning workflow. This reduces the need for manual intervention from the data science team,
                                        making the process more efficient and streamlined.
        -> Accelerate Deployment: The pipline helps reduce the time data and models take to the production phase. This enables faster deployment of machine learning solutions and
                                        quicker integration into real-world applications
        -> Enable focus on innovation: With modular components and automation in place, the pipline frees the data science team to focus more on developing new solutions rather than
                                        spending excessive time maintaining existing ones.
        -> Facilitate reusability: Specific steps can be reused to develop and deploy end-to-end solutions, allowing for seamless integration with existing systems without the need
                                        to start from scratch each time. 
