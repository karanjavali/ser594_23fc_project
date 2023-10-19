import matplotlib.pyplot as plt
import json
import sys

def scatter_plot_distribution(code1, code2, number):
    with open("./data_processed/nutrient_food_data.json", "r") as file:
        nutrient_data = json.load(file)
    with open("./data_processed/nutrient_codes.json", "r") as file:
        nutrient_codes = json.load(file)
        

    code1_content = [n['amount'] for n in nutrient_data[code1]]
    code1_unit = nutrient_data[code1][0]['unitName']
    code2_content = [n['amount'] for n in nutrient_data[code2]]
    code2_unit = nutrient_data[code2][0]['unitName']
    plt.scatter(code1_content, code2_content, color='r', marker='o')
    plt.xlabel(nutrient_codes[code1] + '(in {})'.format(code1_unit))
    plt.ylabel(nutrient_codes[code2] + '(in {})'.format(code2_unit))
    plt.title('Nutrient pair scatterplot')
    plt.grid(False) 
    plt.savefig('visuals/scatter_{}.png'.format(number))
    plt.show()

def calculate_statistics(nutrient_id):
    with open("./data_processed/nutrient_food_data.json", "r") as file:
        nutrient_data = json.load(file)
    
    unit = nutrient_data[nutrient_id][0]['unitName']
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


if __name__ == "__main__":
# protein_cabs_distribution()
    output = 'Qualitative Feature - Nutrition occurence in different ingredients\nQuantitative features - Protein content(in grams), Total Carbohydrates (in grams), Total Calories (in KCAL)\n\n'
    nutrient_codes = ['203', '205', '208']
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