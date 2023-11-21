import json
import pandas as pd
from sklearn.model_selection import train_test_split
import wf_ml_prediction, wf_ml_training
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
with open('./models/x_train.pkl', 'wb') as file:
    pickle.dump(x_train, file)

with open('./models/x_test.pkl', 'wb') as file:
    pickle.dump(x_test, file)

with open('./models/y_train.pkl', 'wb') as file:
    pickle.dump(y_train, file)

with open('./models/y_test.pkl', 'wb') as file:
    pickle.dump(y_test, file)
wf_ml_training.train_models()
wf_ml_prediction.evaluate_models()