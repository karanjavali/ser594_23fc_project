1. NutriGen - An ingredient picker!
2. Author - Karan Navin Javali 
3. Date of submission - 10/18/2023

4.

1. Answer basic questions

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

2. Look for interpretable records

"fdc_id","food_code","wweia_category_code","start_date","end_date"
"2340775","11121100","1002","2019-01-01","2020-12-31"
"2340776","11121210","1006","2019-01-01","2020-12-31"

This row does not make much sense to most people. However, we are concerned with the fdc_id column, which contains the IDs of the ingredients I will be using. Other columns are irrelevant. Hence, the rows are reasonable.




5.

