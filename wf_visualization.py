import matplotlib.pyplot as plt
import json

def protein_cabs_distribution():
    with open("./data_processing/nutrient_food_data.json", "r") as file:
        nutrient_data = json.load(file)

    protein_code = '203'
    carbohydrates_code = '205'

    protein_content = [n['amount'] for n in nutrient_data[protein_code]]
    carb_content = [n['amount'] for n in nutrient_data[carbohydrates_code]]

    plt.scatter(protein_content, carb_content, color='r', marker='o')
    plt.xlabel('Carbohydrates')
    plt.ylabel('Protein')
    plt.title('Protein-Carbohydrate distribution per 100 gm of ingredient')
    plt.grid(False) 
    # plt.savefig('hw03_javali_image2scatterplot.png')
    plt.show()

protein_cabs_distribution()