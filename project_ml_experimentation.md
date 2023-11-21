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

**Justification:** Based on the scatter plot (Carbohydrate vs Lipid), the 2 have a non linear inverse relationship to a certain extent if one of them reaches high values. Hence this could be an indicator that high carb foods will have low fat and low carb foods will have high amounts of fat. 

## Experiments 
### Varying A
**Prediction Trend Seen:**
High calories value input - To predict the fat content (in gm) of food with nutrition value of 20 kcal, 30 gm protein, and 30 gm carbohydrates.
Using Random Forest Model -  0.31770000000000015  gm

Low calories value input - To predict the fat content (in gm) of food with nutrition value of 600 kcal, 30 gm protein, and 30 gm carbohydrates.
Using Random Forest Model -  50.977999999999994  gm

As mentioned above, the fat content increases with increase in calorie content.

### Varying B
**Prediction Trend Seen:**

High calories value input - To predict the fat content (in gm) of food with nutrition value of 400 kcal, 10 gm protein, and 85 gm carbohydrates.
Using Random Forest Model -  3.6326999999999963  gm


Low calories value input - To predict the fat content (in gm) of food with nutrition value of 400 kcal, 10 gm protein, and 2 gm carbohydrates.
Using Random Forest Model -  33.82199999999998  gm

As mentioned above, the values inversely change.

### Varying A and B together
**Prediction Trend Seen:**
High calories and high carbohydrates value input - To predict the fat content (in gm) of food with nutrition value of 600 kcal, 30 gm protein, and 85 gm carbohydrates.
Using Random Forest Model -  33.17799999999997  gm

Low calories and low carbohydrates value input - To predict the fat content (in gm) of food with nutrition value of 20 kcal, 30 gm protein, and 2 gm carbohydrates.
Using Random Forest Model -  0.5424000000000003  gm

When both increase, the fat content increases and vice versa. The increase (caused by calories) is greater than the decrease (caused by carbohydrates)


### Varying A and B inversely
**Prediction Trend Seen:**
High calories and low carbohydrates value input - To predict the fat content (in gm) of food with nutrition value of 600 kcal, 30 gm protein, and 2 gm carbohydrates.
Using Random Forest Model -  57.17399999999995  gm

Low calories and high carbohydrates value input - To predict the fat content (in gm) of food with nutrition value of 20 kcal, 30 gm protein, and 85 gm carbohydrates.
Using Random Forest Model -  0.31770000000000015  gm

Varying the features inversely causes dramatic change in fat content. When increasing calorie content and reducing carbohydrates, the increase is caused from both features and vice versa.
