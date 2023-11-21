#### SER594: Machine Learning Evaluation
#### Title - IngriGen - The Ingredient Picker
#### Author - Karan Navin Javali
#### Date - 11/20/2023

## Evaluation Metrics
### Metric 1
**Name:** Mean Squared Error (MSE)

**Choice Justification:** MSE is chosen as it measures the average squared difference between the predicted and actual values. For the fat content prediction (in gm), minimizing the squared differences is crucial, and MSE provides a clear and interpretable measure of model accuracy.

**Interpretation:** The closer the MSE is to zero, the better the model's performance. In the context of the fat content prediction, a lower MSE indicates that the model's predictions are closer to the actual fat contents.

### Metric 2
**Name:** R-squared (R2)

**Choice Justification:** R-squared is chosen as it provides a measure of how well the model explains the variance in the target variable. For fat content prediction, a high R-squared value indicates that a large proportion of the variability in fat contents is captured by the model.

**Interpretation** R-squared ranges from 0 to 1, where 1 indicates a perfect fit. In the context of fat content prediction, an R-squared value close to 1 signifies a strong ability of the model to explain the variability in fat contents.

## Alternative Models
### Alternative 1 - Decision Tree Regressor
**Construction:** The Decision Tree Regressor is constructed as a single decision tree. It is a non-linear model that recursively splits the data based on features to make predictions.

**Evaluation:** The Decision Tree Regressor has a higher MSE and a slightly lower R-squared compared to the Random Forest model. It captures complex relationships in the data but may be prone to overfitting.

### Alternative 2 - Gradient Boosting Regressor
**Construction:** The Gradient Boosting Regressor is constructed as an ensemble of weak learners (usually decision trees). It builds trees sequentially, with each tree correcting the errors of the previous ones.

**Evaluation:** The Gradient Boosting Regressor has a higher MSE and a slightly lower R-squared compared to the Random Forest model. While it is powerful, it may require careful hyperparameter tuning to prevent overfitting.

### Alternative 3 - SVM with RBF Kernel
**Construction:** The SVM with RBF Kernel is constructed as a support vector machine with a radial basis function (RBF) kernel. It is capable of capturing non-linear relationships in the data.

**Evaluation:** The SVM with RBF Kernel has a significantly higher MSE and a lower R-squared compared to the Random Forest model. SVMs can be sensitive to hyperparameter choices and may not perform as well in this context.

### Best Model - Random Forest
### Alternative Best Model - Decision Tree Regressor
**Reason** The Decision Tree Regressor model outperforms the alternative models in terms of both MSE and R-squared. It has the second best performance after Random Forest Model. It provides a good balance between accuracy and generalization, making it the best-performing model (among the alternative choices) for fat content prediction in this context.