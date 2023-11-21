import json
import pandas as pd
from sklearn.model_selection import train_test_split
import wf_ml_prediction, wf_ml_training
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np
with open("./data_processed/food_data.json", "r") as file:
    food_data = json.load(file)
with open("./data_processed/food_id_name.json", "r") as file:
    food_id_name = json.load(file)

data_json = []
for f in food_data:
    obj = {}
    obj['ingredient'] = food_id_name[f]
    obj['protein'] = [obj for obj in food_data[f] if obj["number"] == "203"][0]["amount"]
    obj['calories'] = [obj for obj in food_data[f] if obj["number"] == "208"][0]["amount"]
    obj['carbohydrates'] = [obj for obj in food_data[f] if obj["number"] == "205"][0]["amount"]
    obj['fat'] = [obj for obj in food_data[f] if obj["number"] == "204"][0]["amount"]
    data_json.append(obj)

data = pd.DataFrame(data_json)

features = data[['carbohydrates', 'protein', 'calories']]
targets = data[['fat']]

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(features, targets, test_size=0.2, random_state=16)
y_train = np.ravel(y_train)
y_test = np.ravel(y_test)
# save the sets in the models folder
with open('./data_processed/x_train.pkl', 'wb') as file:
    pickle.dump(x_train, file)

with open('./data_processed/x_test.pkl', 'wb') as file:
    pickle.dump(x_test, file)

with open('./data_processed/y_train.pkl', 'wb') as file:
    pickle.dump(y_train, file)

with open('./data_processed/y_test.pkl', 'wb') as file:
    pickle.dump(y_test, file)


def evaluate_mse_and_r2():
    
    with open('./data_processed/x_test.pkl', 'rb') as file:
        x_test = pickle.load(file)
    with open('./data_processed/x_train.pkl', 'rb') as file:
        x_train = pickle.load(file)
    with open('./data_processed/y_test.pkl', 'rb') as file:
        y_test = pickle.load(file)

    with open('./models/rf_model.pkl', 'rb') as file:
        rf_model = pickle.load(file)
    with open('./models/dt_model.pkl', 'rb') as file:
        dt_model = pickle.load(file)
    with open('./models/gb_model.pkl', 'rb') as file:
        gb_model = pickle.load(file)
    with open('./models/svm_model.pkl', 'rb') as file:
        svm_model = pickle.load(file)
    evaluation_result = 'Evaluation Summary\n'

    scaler = StandardScaler()
    scaler.fit(x_train)
    x_test_scaled = scaler.transform(x_test)

    # Random Forest
    rf_predictions = rf_model.predict(x_test)
    rf_mse = mean_squared_error(y_test, rf_predictions)
    rf_r2 = r2_score(y_test, rf_predictions)
    print(f'Random Forest Model Mean Squared Error: {rf_mse}\nRandom Forest Model R-squared value: {rf_r2}\n')
    evaluation_result += f'Random Forest Model Mean Squared Error: {rf_mse}\nRandom Forest Model R-squared value: {rf_r2}\n'

    # Decision Tree Regressor
    dt_predictions = dt_model.predict(x_test)
    dt_mse = mean_squared_error(y_test, dt_predictions)
    dt_r2 = r2_score(y_test, dt_predictions)
    print(f'Decision Tree Regressor Model Mean Squared Error: {dt_mse}\nDecision Tree Regressor Model R-squared value: {dt_r2}\n')
    evaluation_result += f'Decision Tree Regressor Model Mean Squared Error: {dt_mse}\nDecision Tree Regressor Model R-squared value: {dt_r2}\n'

    # Gradient Boosting Regressor
    gb_predictions = gb_model.predict(x_test)
    gb_mse = mean_squared_error(y_test, gb_predictions)
    gb_r2 = r2_score(y_test, gb_predictions)
    print(f'Gradient Boosting Regressor Model Mean Squared Error: {gb_mse}\nGradient Boosting Regressor Model R-squared value: {gb_r2}\n')
    evaluation_result += f'Gradient Boosting Regressor Model Mean Squared Error: {gb_mse}\nGradient Boosting Regressor Model R-squared value: {gb_r2}\n'

    # SVM with RBF Kernel
    svm_predictions = svm_model.predict(x_test_scaled)
    svm_mse = mean_squared_error(y_test, svm_predictions)
    svm_r2 = r2_score(y_test, svm_predictions)
    print(f'SVM with RBF Kernel Model Mean Squared Error: {svm_mse}\nSVM with RBF Kernel Model R-squared value: {svm_r2}\n')
    evaluation_result += f'SVM with RBF Kernel Model Mean Squared Error: {svm_mse}\nSVM with RBF Kernel Model R-squared value: {svm_r2}\n'

    with open("./evaluation/summary.txt", 'w') as file:
        file.write(evaluation_result)

# wf_ml_training.train_models()
# evaluate_mse_and_r2()
wf_ml_prediction.predict_output()