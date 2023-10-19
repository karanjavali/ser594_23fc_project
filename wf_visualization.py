import matplotlib.pyplot as plt
import numpy as np
import json
import sys

def scatter_plot_distribution(code1, code2, number):
    with open("./data_processed/nutrient_food_data.json", "r") as file:
        nutrient_data = json.load(file)
    with open("./data_processed/nutrient_codes.json", "r") as file:
        nutrient_codes = json.load(file)
    with open("./data_processed/nutrient_units.json", "r") as file:
        nutrient_units = json.load(file)
        

    code1_content = [n['amount'] for n in nutrient_data[code1]]
    code1_unit = nutrient_units[code1]
    code2_content = [n['amount'] for n in nutrient_data[code2]]
    code2_unit = nutrient_units[code2]


    plt.scatter(code1_content, code2_content, alpha=0.7, cmap='viridis', edgecolors='k', linewidths=1.5)
    plt.xlabel(nutrient_codes[code1] + '(in {})'.format(code1_unit))
    plt.ylabel(nutrient_codes[code2] + '(in {})'.format(code2_unit))
    plt.title('Nutrient pair scatterplot')

    plt.grid(linestyle='--', alpha=0.5)
    plt.savefig('visuals/scatter_{}.png'.format(number))
    plt.show()


def calculate_statistics(nutrient_id):
    with open("./data_processed/nutrient_food_data.json", "r") as file:
        nutrient_data = json.load(file)
    with open("./data_processed/nutrient_units.json", "r") as file:
        nutrient_units = json.load(file)
    
    unit = nutrient_units[nutrient_id]
    nutrient_content = [n['amount'] for n in nutrient_data[nutrient_id]]
    nutrient_content = sorted(nutrient_content)
    # print(nutrient_content)
    min, max = nutrient_content[0], nutrient_content[-1]
    # print(min,max)
    median = nutrient_content[len(nutrient_content)//2]
    # print(median)
    return min, max, median, unit
    

def calculate_nutrient_frequency():
    with open("./data_processed/nutrient_food_data.json", "r") as file:
        nutrient_data = json.load(file)
    with open("./data_processed/nutrient_codes.json", "r") as file:
        nutrient_codes = json.load(file)
    
    num_categories = len(nutrient_codes)
    min_occuring_num, max_occuring_num = sys.maxsize, -1
    min_occuring_category, max_occuring_category = '',''

    for n in nutrient_data:
        num_occurence = 0
        for x in nutrient_data[n]:
            if x['amount'] > 0.0:
                num_occurence += 1
        
        if num_occurence < min_occuring_num:
            min_occuring_num = num_occurence
            min_occuring_category = nutrient_codes[n]
        
        if num_occurence > max_occuring_num:
            max_occuring_num = num_occurence
            max_occuring_category = nutrient_codes[n]
        
    return num_categories, max_occuring_category, max_occuring_num, min_occuring_category, min_occuring_num


def plot_histogram():
    with open("./data_processed/nutrient_food_data.json", "r") as file:
        nutrient_data = json.load(file)
    with open("./data_processed/nutrient_codes.json", "r") as file:
        nutrient_codes = json.load(file)
    
    names = []
    values = []
    val = {}
    for n in nutrient_data:
        num_occurence = 0
        for x in nutrient_data[n]:
            if x['amount'] > 0.0:
                num_occurence += 1
        names.append(nutrient_codes[n])
        values.append(num_occurence)
        val[nutrient_codes[n]] = num_occurence
    
    plt.figure(figsize=(25, 35)) 
    
    values = sorted(values)
    print(values)
    plt.barh(names, values, edgecolor='black', alpha=0.7)
    plt.ylabel("Nutrient Name") 
    plt.xlabel("Occurence in ingredients") 
    plt.title("Histogram of Nutrient occurence in the ingredients") 


    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.savefig('visuals/hist_occurences.png')
    plt.show()



if __name__ == "__main__":
    
    output = 'Qualitative Feature - Nutrition occurence in different ingredients\nQuantitative features - Protein content(in grams), Total Carbohydrates (in grams), Total Calories (in KCAL)\n\n'
    nutrient_codes = ['203', '205', '208'] # Protein, Carbohydrates, Calories
    nutrients_chosen = ['Protein', 'Carbohydrate', 'Calories']
    for i in range(len(nutrient_codes)):

        output += '\n{} content statistics\n'.format(nutrients_chosen[i])
        min, max, median, unit = calculate_statistics(nutrient_codes[i])
        output += 'Min - {} {}\nMax - {} {}\nMedian - {} {}\n'.format(min,unit,max,unit,median,unit)
  
    output += '\nNutrient occurence statistics:\n '
    num_categories, max_occuring_category, max_occuring_num, min_occuring_category, min_occuring_num = calculate_nutrient_frequency()
    output += '\nNumber of categories(nutrients) - {}\nMax occuring category - {}\nNumber of occurences - {}\nMin occuring category - {}\nNumber of occurences - {}'.format(
        num_categories,
        max_occuring_category,
        max_occuring_num,
        min_occuring_category,
        min_occuring_num
    )
    
    with open("./data_processed/summary.txt", 'w') as file:
        file.write(output)
    
    scatter_plot_distribution('203','205', 1)
    scatter_plot_distribution('205','208', 2)
    scatter_plot_distribution('208','203', 3)
    plot_histogram()