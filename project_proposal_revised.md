#### SER594:- Project Proposal
#### Title :-  IngriGen - A tool to pick ingredients
#### Author :- Karan Navin Javali
#### Date :- 10/30/2023

Keywords: new recipes, calories, ideal ingredients

Description: 

The idea for this project is to analyze nutrition data of different ingredients and select the raw ingredients which, as a recipe will satisfy a requirement. The dataset will contain various fields such as calories per unit weight, fat, vitamin content, etc. This kind of analysis will pick random ingredients (organized by meat, vegetables, oils, flavoring, etc), along with quantity for different requirements such as calorie content, weight, body goal, etc. This could serve as an inspiration to create a new recipe to fulfill that requirement.
The application would ideally pick ingredients in an organized manner, and suggest new recipes.

Research Questions:

RO1: To perform exploratory visualization work on the nutrition data to describe trends within ingredients, including calories per unit weight, fat content, and vitamin content, organized by categories such as meat, vegetables, oils, and flavorings.

RO2: To apply a machine learning technique, either classification or regression, to predict the ideal ingredients and quantities for different requirements, such as calorie content, weight goals, and body goals, based on the nutrition data.

RO3: To defend the model used in RO2 for ingredient selection and quantity prediction, ensuring its reliability and accuracy.

RO4: To assess the ability of the model from RO2 to provide insights into the relationships between different ingredients and their impact on different weight groups and goals, thereby generating knowledge to assist in creating new recipes for various target audiences.

These research objectives will guide the project's focus and provide a clear structure for achieving the desired outcomes.

Intellectual Merit: 

We could gain insights to potential new recipes for different weight groups and weight goals (bulk up, cut down, maintenance, etc). The way this can happen is to learn more about food and divide the ingredients obtained into categories, for example - meat, vegetables, fruits, oil, flavors (different powders, salt, pepper, etc). We can display the total nutrtion provided by the ingredients (with some margin of error). The ingredients will be picked randomly in an organized manner. Note that this is an ingredient picker, and not a recipe generator. The results of this project could be a starting point for new recipes for various target audiences with different requirements. We could use the ingredients on other recipe generator platforms to get the desired results.

Data Sourcing: 

The best database for this would be https://fdc.nal.usda.gov/download-datasets.html, which is the website for the US Department of Agriculture. This website also has APIs to access data. The data needs to be processed to obtain it in our format. I would work primarily with the FNDDS (Food and Nutrient Database for Dietary Studies) foods, which is a database that is used to convert food and beverages consumed in What We Eat In America (WWEIA), National Health and Nutrition Examination Survey (NHANES) into gram amounts and to determine their nutrient values.

Background Knowledge: 

Sources for background understanding

1. USDA National Nutrient Database - https://fdc.nal.usda.gov/ . This website offers detailed data on the nutrient content of a wide range of foods and beverages. This is the primary source of data for the application. I will be using a few of the APIs and the datasets provided in the website.
2. Nutritionix API - Nutritionix (https://www.nutritionix.com/) offers an API that provides access to a vast database of food and restaurant nutrition information, including detailed nutrient breakdowns and serving sizes. This is an alternate data source, which can be handy considering the multitude of services it provides.
3. EuroFIR: EuroFIR (European Food Information Resource) offers a database of food composition data from European countries, including information on nutrients, bioactive compounds, and food additives (https://www.eurofir.org/). This is a future possible extension to the application, which currently focuses on American foods.


Related Work:

1. Rossi L, Ferrari M, Ghiselli A. The Alignment of Recommendations of Dietary Guidelines with Sustainability Aspects: Lessons Learned from Italy's Example and Proposals for Future Development. Nutrients. 2023 Jan 20;15(3):542. doi: 10.3390/nu15030542. PMID: 36771249; PMCID: PMC9921064.

2. Welsh S, Shaw A, Davis C. Achieving dietary recommendations: whole-grain foods in the Food Guide Pyramid. Crit Rev Food Sci Nutr. 1994;34(5-6):441-51. doi: 10.1080/10408399409527674. PMID: 7811377.

3. Zhou L, Zhang C, Liu F, Qiu Z, He Y. Application of Deep Learning in Food: A Review. Compr Rev Food Sci Food Saf. 2019 Nov;18(6):1793-1811. doi: 10.1111/1541-4337.12492. Epub 2019 Sep 16. PMID: 33336958.

4. Barrett EM, Afrin H, Rayner M, Pettigrew S, Gaines A, Maganja D, Jones A, Mozaffarian D, Beck EJ, Neal B, Taylor F, Munn E, Wu JH. Criterion validation of nutrient profiling systems: a systematic review and meta-analysis. Am J Clin Nutr. 2023 Oct 18:S0002-9165(23)66187-8. doi: 10.1016/j.ajcnut.2023.10.013. Epub ahead of print. PMID: 37863430.

5. Miller LM, Cassady DL. The effects of nutrition knowledge on food label use. A review of the literature. Appetite. 2015 Sep;92:207-16. doi: 10.1016/j.appet.2015.05.029. Epub 2015 May 27. PMID: 26025086; PMCID: PMC4499482.

6. Kant AK. Dietary patterns and health outcomes. J Am Diet Assoc. 2004 Apr;104(4):615-35. doi: 10.1016/j.jada.2004.01.010. PMID: 15054348.
