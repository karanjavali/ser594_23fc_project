
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
        'carbohydrates':[40, 1.58, 75.5], 
        'protein':[30, 19, 6.67], 
        'calories':[500, 117, 389]
    })

    rf_prediction = rf_model.predict(model_input)
    dt_prediction = dt_model.predict(model_input)
    gb_prediction = gb_model.predict(model_input)
    svm_prediction = svm_model.predict(model_input)

    print("\nTo predict the fat content (in gm) of food with nutrition value of 500 kcal, 30 gm protein, and 40 gm carbohydrates")
    print("Using Random Forest Model - ", rf_prediction[0], ' gm')
    print("Using Decision Tree Regressor Model - ", dt_prediction[0], ' gm')
    print("Using Gradient Boosting Regressor Model - ", gb_prediction[0], ' gm')
    print("Using SVM with RBF Kernel Model - ", svm_prediction[0], ' gm')
    

    print("\nTo predict the fat content (in gm) of ham with nutrition value of 117 kcal, 19 gm protein, and 1.58 gm carbohydrates. Actual fat content = 3.87 gm")
    print("Using Random Forest Model - ", rf_prediction[1], ' gm')
    print("Using Decision Tree Regressor Model - ", dt_prediction[1], ' gm')
    print("Using Gradient Boosting Regressor Model - ", gb_prediction[1], ' gm')
    print("Using SVM with RBF Kernel Model - ", svm_prediction[1], ' gm')

    
    print("\nTo predict the fat content (in gm) of Snack bar, oatmeal with nutrition value of 389 kcal, 6.67 gm protein, and 75.5 gm carbohydrates. Actual fat content = 6.67 gm")
    print("Using Random Forest Model - ", rf_prediction[2], ' gm')
    print("Using Decision Tree Regressor Model - ", dt_prediction[2], ' gm')
    print("Using Gradient Boosting Regressor Model - ", gb_prediction[2], ' gm')
    print("Using SVM with RBF Kernel Model - ", svm_prediction[2], ' gm')