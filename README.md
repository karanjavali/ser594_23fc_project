IngriGen – ML-Based Nutrition & Ingredient Analysis

IngriGen is a machine learning project that analyzes large-scale food nutrition data to support ingredient selection and recipe creation based on dietary goals. The system predicts fat content using macronutrient information (calories, carbohydrates, protein) and applies data-driven insights to nutrition planning.

🔍 What This Project Does

Processes nutrition data from the USDA FoodData Central (FNDDS) dataset

Performs exploratory data analysis to identify macro-nutrient trends

Trains and evaluates multiple machine learning models

Predicts fat content using a Random Forest model optimized for non-linear data

🧠 Machine Learning Highlights

Models explored: Linear Regression, LASSO, Ridge, SVM, Neural Networks, Decision Trees

Final Model: Random Forest

Performance:

R² ≈ 0.99

MSE ≈ 1.05

Selected Random Forest for its ability to model feature interactions and non-linear relationships while reducing overfitting

📊 Data & Features

Source: USDA FoodData Central API

Key Inputs: Calories, Carbohydrates, Protein

Target: Fat Content

🗂️ Project Structure
data_original/        # Raw nutrition data
data_processed/       # Cleaned datasets
models/               # Trained models
evaluation/           # Model metrics
visuals/               # EDA plots

wf_dataprocessing.py  # Data prep & feature engineering
wf_ml_training.py     # Model training
wf_ml_prediction.py   # Predictions
wf_ml_evaluation.py   # MSE & R² metrics

🛠️ Tech Stack

Python · Pandas · NumPy · Scikit-learn · Random Forest · Data Visualization · USDA API

👤 Author

Karan Navin Javali
