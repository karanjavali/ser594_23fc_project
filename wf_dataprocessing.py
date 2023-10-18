
import requests, csv, json
from wf_constants import GET_FOOD_URL, API_KEY, GET_FOODS_URL
import pandas as pd

def get_data():
    food_list = []
    survey_fndds_foods_df = pd.read_csv('data_original/survey_fndds_food.csv')
    url = GET_FOODS_URL + '?format=abridged&api_key={}&fdcIds='.format(API_KEY)
    url_cpy = url
    for index, row in survey_fndds_foods_df.iterrows():
        # print(index, row['Name'], row['Age'])
        fdc_id = row['fdc_id']
        url += str(fdc_id) + ','
        # url = GET_FOOD_URL + str(fdc_id) + "?format=full?api_key={}".format(API_KEY)
        if index%20 == 0:
            response = requests.get(url[:-1])
            food_list += response.json()
            url = url_cpy
    
    with open("./data_original/food_data_original.json", "w") as file:
        json.dump(food_list, file, indent=4)
    
def generate_nutrition_food_data():
    raw_food_data = []
    with open("./data_original/food_data_original.json", "r") as file:
        raw_food_data = json.load(file)
    raw_food_data = raw_food_data[1:] # removing human milk
    nutrient_codes = {}
    nutrient_food_data = {}
    for food in raw_food_data:
        food_name = food['description']
        food_id = food['fdcId']

        for nutrient in food['foodNutrients']:
            nutrient_number = nutrient['number']
            nutrient_name = nutrient['name']
            amount = nutrient['amount']
            unit_name = nutrient['unitName']

            obj = {
                'name': food_name,
                'id': food_id,
                'amount': amount,
                'unitName': unit_name
            }

            if nutrient_number not in nutrient_food_data:
                nutrient_food_data[nutrient_number] = []

            nutrient_food_data[nutrient_number].append(obj)
            nutrient_codes[nutrient_number] = nutrient_name

    with open("./data_processing/nutrient_food_data.json", "w") as file:
        json.dump(nutrient_food_data, file, indent=4)
    
    with open("./data_processing/nutrient_codes.json", "w") as file:
        json.dump(nutrient_codes, file, indent=4)

def generate_cleaned_food_data():
    raw_food_data = []
    with open("./data_original/food_data_original.json", "r") as file:
        raw_food_data = json.load(file)
    raw_food_data = raw_food_data[1:] # removing human milk
    food_data = {}
    for food in raw_food_data:    
        obj = {}
        obj['name'] = food['description']
        obj['nutrients'] = food['foodNutrients']
        food_data[food['fdcId']] = obj
    
    with open("./data_processing/food_data.json", "w") as file:
        json.dump(food_data, file, indent=4)



# get_data()
generate_nutrition_food_data()
# generate_cleaned_food_data()