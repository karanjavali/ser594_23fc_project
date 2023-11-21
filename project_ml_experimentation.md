#### SERX94: Experimentation
#### Title - IngriGen - The Ingredient Picker
#### Author - Karan Navin Javali
#### Date - 11/20/2023


## Explainable Records
### Record 1
**Raw Data:** food_id = 2341283
{
    'protein': 19.0,
    'carbohydrates': 1.58,
    'calories': 117
}
Prediction Explanation:** 
To predict the fat content (in gm) of ham with nutrition value of 117 kcal, 19 gm protein, and 1.58 gm carbohydrates. Actual fat content = 3.87 gm
Using Random Forest Model -  4.104399999999997  gm

The predicted fat content is 4.10 gm. The Random Forest model takes into account the non-linear relationships between nutrients and accurately predicts the fat content based on the given nutrition values. It considers complex interactions between features, due to which the output is reliable.

### Record 2
**Raw Data:** in food_data, id = 2343583.
{
    'protein': 6.67,
    'carbohydrates': 75.5,
    'calories': 389
}

Prediction Explanation:**
To predict the fat content (in gm) of Snack bar, oatmeal with nutrition value of 389 kcal, 6.67 gm protein, and 75.5 gm carbohydrates. Actual fat content = 6.67 gm
Using Random Forest Model -  6.430599999999997  gm

The predicted fat content is 6.43 gm. The Random Forest model considers the interactions between nutrients and provides a reasonable prediction that aligns well with the actual fat content.

## Interesting Features
### Feature A
**Feature:** Calories

**Justification:** Based on the scatter plot (Energy vs Lipid) created previously, the fat content of ingredients increases with the increase in calorie content of the food and vice versa. Hence with the fluctuation of calorie content of the food, the fat content would also greatly vary. Based on the trend, low calorie foods generally contain lower fat content overall.

### Feature B
**Feature:** Carbohydrates

**Justification:** Based on the scatter plot (Carbohydrate vs Lipid), the 2 have inverse relationship to a certain extent if one of them reaches high values. Hence this could be an indicator that high carb foods will have low fat and low carb foods will have high amounts of fat.

## Experiments 
### Varying A
**Prediction Trend Seen:** TODO

### Varying B
**Prediction Trend Seen:** TODO

### Varying A and B together
**Prediction Trend Seen:** TODO


### Varying A and B inversely
**Prediction Trend Seen:** TODO

(duplicate above as many times as needed; remove this line when done)