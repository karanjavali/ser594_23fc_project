from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

import pickle


def train_models():

    with open('./models/x_train.pkl', 'rb') as file:
        x_train = pickle.load(file)

    with open('./models/y_train.pkl', 'rb') as file:
        y_train = pickle.load(file)

    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    
    linear_model = LinearRegression()
    linear_model.fit(x_train_scaled, y_train)

    with open('./models/linear_model.pkl', 'wb') as f:
        pickle.dump(linear_model, f)


    ridge_model = Ridge(alpha=0.01)
    ridge_model.fit(x_train_scaled, y_train)

    with open('./models/ridge_model.pkl', 'wb') as f:
        pickle.dump(ridge_model, f)


    lasso_model = Lasso(alpha=0.01)
    lasso_model.fit(x_train_scaled, y_train)


    with open('./models/lasso_model.pkl', 'wb') as f:
        pickle.dump(lasso_model, f)

    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(x_train, y_train)

    with open('./models/rf_model.pkl', 'wb') as f:
        pickle.dump(rf_model, f)