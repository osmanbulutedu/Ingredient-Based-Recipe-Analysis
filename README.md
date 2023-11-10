# Ingredient-Based-Recipe-Analysis

### Abstract

This project addresses the evaluation of online recipe healthiness through machine learning, feature engineering, and data processing. It leverages the RecipeKG knowledge graph, incorporating web scraping from allrecipes.com, unit normalization, and ingredient vectorization. The objectives encompass structured data creation, health score prediction using Classification and Regression techniques, and emphasizing ingredient amounts' significance. Results highlight the Histogram-Based Gradient Boosting model's performance, offering a valuable tool for informed dietary choices and open-source datasets for further research in online culinary diversity.

 


### Prerequisites
Python 3.8 or above and the following libraries

```
- request, json, BeautifulSoup
- nltk, glob, difflib
- rdflib
```


### Files
```
  Academic paper:
       ➡️Ingrediet Based Recipe Health Analysis.pdf : The detailed academic paper form of the whole project

  Code:
   
      ➡️ queryIngUnitQuant.ipynb : This code has a query, that takes Recipe,Ingredients, Ingredients Quantity and Units and convert them to a data frame RecipeKG knowledge graph (https://github.com/IDIASLab/RecipeKG).

      ➡️ querynutrient.ipynb : This code has a query that takes all nutrients and their recipes' category from RecipeKG knowledge graph (https://github.com/IDIASLab/RecipeKG).

      ➡️ initial_functions.py : This code has some functions used in the other codes. Explanations are on top of each function.

      ➡️ scrape servings.ipynb : This code scrape serving per recipe information from allrecipes.com for more than 70k recipe URLs.

      ➡️ PreProcessing_1.ipynb: First part of the preprocessing is applied in this code. Explanation of each step is in the code.

      ➡️ pack_can_jar_to_oz.ipynb: For units of "pack", "can" and "jar", "oz" equivalences are scraped from corresponding recipe urls of allrecipe.com

      ➡️ unit conversion and ML.ipynb: Unit conversion and then all the ML experiments is in this code. Different configurations can easily be tried in the last part of the code. Further explanations are in the code.
      

  

   Data:
      ➡️ ingUnitQuant.csv, nutrient.csv, recipes-scores.csv are the main data obtained by RecipeKG(https://github.com/IDIASLab/RecipeKG) project by using sparql queries.
      ➡️ servings.csv : serving size information of recipes scraped from allrecipes.com. This data is the output of scrape servings.ipynb
      ➡️ packcanjar_oz.csv: output of pack_can_jar_to_oz.ipynb:
      ➡️ recipe40k.csv: intermediate data of the project, after some preprocessing. The output of PreProcessing_1.jpynb
      ➡️ final_recipe.csv: The final data after all preprocessing. 33.5k recipe, 423 unique ingredients. (287685 rows × 20 columns)
             ➡️ newQuant column: the quantity per serving not per whole recipe
             ➡️ newUnit column: the units are in either 'cup', 'ounce' or 'piece'
      
       
   
```     




### Contributions 
We encourage the collaborative extention of our work. To simplify the process we monitor this repository's Issue tracker for requests of new terms/classes. We also check for reported errors or specific concerns related to the data.
