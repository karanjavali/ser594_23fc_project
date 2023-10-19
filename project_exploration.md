1. IngriGen - The ingredient picker
2. Author - Karan Navin Javali 
3. Date of submission - 10/18/2023

4. Basic Questions and Interpretable Records

- Basic Questions

Author of dataset - US Department of Agriculture
Released on - 04/2023
Files used - survey_fndds_food.csv
Number of records - 5625

MD5 of file - edf3db086237e679e1026b67ece932d4
Download link - https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_csv_2023-04-20.zip
NOTE - Only survey_fndds_food.csv was used from this folder.

Columns and their meaning -

fdc_id - ID of the food in the food table
food_code - A unique ID identifying the food within FNDDS
wweia_category_number - Unique Identification number for WWWEIA food category to which this food is assigned.
start_date - Start date indicates time period corresponding to WWWEIA data
end_date - End date indicates time period corresponding to WWWEIA data

The dataset is not synthetic. It contains records collected and compiled by the USDA. The new knowledge I will be generating will be the relationship between different nutrients. For example, the ingredient picker will need to balance out carbs and protein in a diet based on input.

- Look for interpretable records

"fdc_id","food_code","wweia_category_code","start_date","end_date"
"2340775","11121100","1002","2019-01-01","2020-12-31"
"2340776","11121210","1006","2019-01-01","2020-12-31"

The selected rows from the survey food data provide information about different food items. The main identifier here is the fdc_id, which is the id of the ingredient. The other data is related to other databases - food_code (A unique ID identifying the food within FNDDS), wweia_category_code (Unique Identification number for WWEIA food category to which this food is assigned). The start_date and end_date indicates time period corresponding to WWEIA data. For the use of this project, we need the fdc_ids of the ingredients, after which we are calling an API from the USDA to get our relevant data.


5. Background Domain Knowledge

The culinary world is a diverse and dynamic realm, reflecting an astonishing variety of flavors, textures, and cultural influences. It is a space where ingredients hold the power to transform the simplest of dishes into a culinary masterpiece. However, for both amateur and professional cooks, sourcing the right ingredients for a new recipe can often be a challenging and time-consuming endeavor. This is where the data science project, the "IngriGen" steps in to streamline the process and inspire the inner chef in everyone.

The domain of this project revolves around simplifying the art of cooking by providing an innovative solution to a common problem: ingredient selection. Whether it's a seasoned chef looking for fresh inspiration or a novice cook seeking new ideas, IngriGen aims to make the ingredient selection process more educational, and help create new recipes. The purpose of this project is to create inspirations for new recipes and track their nutrition.

Key aspects of this project domain include:

1. Ingredient Variety: The world of culinary ingredients is vast and diverse. This project caters to a wide range of ingredients, spanning vegetables, fruits, proteins, spices, herbs, condiments, and more. It recognizes that each ingredient holds unique characteristics and culinary potential.

2. Randomness: This project can help generate new recipes since the ingredients are picked randomly.

3. Restrictions: This project will have features to pick ingredients based on a restricted amount of nutrients such as calories, fat, protein, etc.

In a world where time is a precious commodity and the desire to explore diverse cuisines is ever-present, the Ingredient Picker empowers individuals to create new meals with ease. By leveraging data science and machine learning, it becomes a versatile and dynamic tool for culinary enthusiasts, connecting them with the world of ingredients and flavors in an engaging and convenient manner.

This project is a bridge between culinary curiosity and the culinary journey. It celebrates the culinary world's diversity, educates users, and, most importantly, turns ingredient selection into an enjoyable and seamless experience. As I move forward in this project, my focus is to make the kitchen a place where creativity and exploration thrive, all within 
the grasp of a user's fingertips.

Sources of information - 

1. USDA National Nutrient Database - https://fdc.nal.usda.gov/ . This website offers detailed data on the nutrient content of a wide range of foods and beverages. I have picked my data from this website. For the purpose of the project, I am making use of FNDDS Data (Foods whose consumption is measured by the What We Eat In America dietary survey component of the National Health and Nutrition Examination Survey (NHANES). Survey nutrient values are usually calculated from Branded and SR Legacy data.)
2. Nutritionix API - Nutritionix (https://www.nutritionix.com/) offers an API that provides access to a vast database of food and restaurant nutrition information, including detailed nutrient breakdowns and serving sizes. This website gives a good idea of how my project would look.
3. Supercook - https://www.supercook.com/#/desktop: This website has good UX. There is an option to pick ingredients and search for recipes. I want to have the ability to save recipes and load them. This can be a good reference to create such a functionality. 


6. No data transformations applied

7. Visualizations

- Protein - Carbohydrate plot: Most of the ingredients with high carbohydrates have low protein. There are vey few ingredients with low carbohydrate content and high protein content.
- Energy - Carbohydrate plot: There seems to be a threshold for amount of energy present with respect to carbohydrates (a clear line is seen above which most values are concentrated). There are very few outliers which do not obey this threshold (high carbohydrate with low energy).
- Protein - Energy plot: There seems to be no relationship of protein and energy amounts except that there is an upper limit for the amount of protein with respect to energy (can be seen as the top slope of the plot).
- Protein - Fat plot: There is no relationship between the amount of protein and fat in the ingredient. The values seem to be random.  It can be seen that there is no ingredient with high amount of fat and protein.
- Carbohydrate - Fat plot: Most ingredients are concentrated in 0-40 gm (fat) range. It can be seen that there is no ingredient with high amount of fat and carbohydrates.
- Fat - Energy plot: With increase in fat, there is an increase in energy. The values are restricted between 2 slopes.

