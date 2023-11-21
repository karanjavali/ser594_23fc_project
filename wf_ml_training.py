from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.preprocessing import StandardScaler

import pickle
from sklearn.svm import SVR

from sklearn.tree import DecisionTreeRegressor


def train_models():

    with open('./data_processed/x_train.pkl', 'rb') as file:
        x_train = pickle.load(file)

    with open('./data_processed/y_train.pkl', 'rb') as file:
        y_train = pickle.load(file)

    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)

    # Random Forest
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(x_train, y_train)
    with open('./models/rf_model.pkl', 'wb') as f:
        pickle.dump(rf_model, f)


    # Decision Tree Regressor
    dt_model = DecisionTreeRegressor(random_state=42)
    dt_model.fit(x_train, y_train)
    with open('./models/dt_model.pkl', 'wb') as f:
        pickle.dump(dt_model, f)


    # Gradient Boosting Regressor
    gb_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
    gb_model.fit(x_train, y_train)
    with open('./models/gb_model.pkl', 'wb') as f:
        pickle.dump(gb_model, f)

    # SVM with RBF Kernel
    svm_model = SVR(kernel='rbf')
    svm_model.fit(x_train_scaled, y_train)
    with open('./models/svm_model.pkl', 'wb') as f:
        pickle.dump(svm_model, f)