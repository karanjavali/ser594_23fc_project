from sklearn.metrics import mean_squared_error
import pickle
from sklearn.preprocessing import StandardScaler
def evaluate_models():
    
    with open('./models/x_test.pkl', 'rb') as file:
        x_test = pickle.load(file)
    with open('./models/x_train.pkl', 'rb') as file:
        x_train = pickle.load(file)
    with open('./models/y_test.pkl', 'rb') as file:
        y_test = pickle.load(file)
    with open('./models/linear_model.pkl', 'rb') as file:
        linear_model = pickle.load(file)
    with open('./models/ridge_model.pkl', 'rb') as file:
        ridge_model = pickle.load(file)
    with open('./models/lasso_model.pkl', 'rb') as file:
        lasso_model = pickle.load(file)
    with open('./models/rf_model.pkl', 'rb') as file:
        rf_model = pickle.load(file)


    scaler = StandardScaler()
    scaler.fit(x_train)
    x_test_scaled = scaler.transform(x_test)

    # Linear Regression
    linear_predictions = linear_model.predict(x_test_scaled)
    linear_mse = mean_squared_error(y_test, linear_predictions)
    print(f'Linear Model Mean Squared Error: {linear_mse}')

    # Ridge Regression
    ridge_predictions = ridge_model.predict(x_test_scaled)
    ridge_mse = mean_squared_error(y_test, ridge_predictions)
    print(f'Ridge Model 1 Mean Squared Error: {ridge_mse}')

    # LASSO Regression
    lasso_predictions = lasso_model.predict(x_test_scaled)
    lasso_mse = mean_squared_error(y_test, lasso_predictions)
    print(f'Lasso Model 2 Mean Squared Error: {lasso_mse}')

    # Random Forest
    rf_predictions = rf_model.predict(x_test)
    rf_mse = mean_squared_error(y_test, rf_predictions)
    print(f'Random Forest Model 3 Mean Squared Error: {rf_mse}')