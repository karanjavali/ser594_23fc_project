
import pickle
import pandas as pd

def predict_output():

    with open('./models/rf_model.pkl', 'rb') as file:
        rf_model = pickle.load(file)
    with open('./models/dt_model.pkl', 'rb') as file:
        dt_model = pickle.load(file)
    with open('./models/gb_model.pkl', 'rb') as file:
        gb_model = pickle.load(file)
    with open('./models/svm_model.pkl', 'rb') as file:
        svm_model = pickle.load(file)


    model_input = pd.DataFrame({
        'carbohydrates':[40], 
        'protein':[30], 
        'calories':[500]
    })

    print("\nTo predict the fat content (in gm) of food with nutrition value of 500 kcal, 30 gm protein, and 25 gm carbohydrates")
    print("Using Random Forest Model - ", rf_model.predict(model_input)[0])
    print("Using Decision Tree Regressor Model - ", dt_model.predict(model_input)[0])
    print("Using Gradient Boosting Regressor Model - ", gb_model.predict(model_input)[0])
    print("Using SVM with RBF Kernel Model - ", svm_model.predict(model_input.values)[0])
