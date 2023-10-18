
import requests, csv, json
from wf_constants import GET_FOOD_URL, API_KEY, GET_FOODS_URL
import pprint
import pandas as pd

def generate_relevant_csv():

    survey_fndds_foods_df = pd.read_csv('data_original/survey_fndds_food.csv')
    print(survey_fndds_foods_df.head())
    food_nutrient_df = pd.read_csv('data_original/food_nutrient.csv', low_memory=False)

    food_df = pd.read_csv('data_original/food.csv')

    survey_foods = pd.merge(survey_fndds_foods_df[['fdc_id']],food_df[['fdc_id','description']], on='fdc_id', how='inner')
    print(survey_foods.head())
    survey_foods_nutrition = pd.merge(survey_fndds_foods_df[['fdc_id']],food_nutrient_df[['fdc_id','nutrient_id','amount']], on='fdc_id', how='inner')
    print(survey_foods_nutrition.head())

    survey_foods.to_csv('data_processing/survey_foods.csv', index=False)
    survey_foods_nutrition.to_csv('data_processing/survey_foods_nutrition.csv', index=False)

    nutrient_df = pd.read_csv('data_original/nutrient.csv')
    nutrient_df[['id','name','unit_name']].to_csv('data_processing/nutrition.csv', index=False)


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
            print(response)
            food_list += response.json()
            url = url_cpy
    
    with open("./data_original/food_data_original.json", "w") as file:
        json.dump(food_list, file, indent=4)
    
def generate_objects():
    
    # Sample DataFrame
    data = {'ID': [1, 1, 2, 2, 3],
            'Value': ['A', 'B', 'C', 'D', 'E']}

    df = pd.DataFrame(data)

    # Group by 'ID' and aggregate 'Value' into a list
    grouped_df = df.groupby('ID')['Value'].agg(list)

    print(grouped_df)
    
    return

get_data()
# generate_relevant_csv()

# generate_objects()