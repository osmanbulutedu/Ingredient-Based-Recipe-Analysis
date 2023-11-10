# Ingredient-Based-Recipe-Analysis
project is going on, files and explanations will be updated
First the files will be explained

### Prerequisites
Python 3.8 or above and the following libraries

```
- request, json, BeautifulSoup
- nltk, glob, difflib
- rdflib
```


### Files
```
  Code:
   
      queryIngUnitQuant.ipynb : This code has a query, that takes Recipe,Ingredients, Ingredients Quantity and Units and convert them to a data frame RecipeKG knowledge graph (https://github.com/IDIASLab/RecipeKG).

      querynutrient.ipynb : This code has a query that takes all nutrients and their recipes' category from RecipeKG knowledge graph (https://github.com/IDIASLab/RecipeKG).

      initial_functions.py : This code has some functions used in the other codes. Explanations are on top of each function.

      scrape servings.ipynb : This code scrape serving per recipe information from allrecipes.com for more than 70k recipe URLs.

      PreProcessing_1.ipynb: First part of the preprocessing is applied in this code. Explanation of each step is in the code.

      pack_can_jar_to_oz.ipynb: For units of "pack", "can" and "jar", "oz" equivalences are scraped from corresponding recipe urls of allrecipe.com

      unit conversion and ML.ipynb: Unit conversion and then all the ML experiments is in this code. Different configurations can easily be tried in the last part of the code. Further explanations are in the code.
      

  

   Data: 
   
```     

### Abstract
This project addresses the evaluation of online recipe healthiness through machine learning, feature engineering, and data processing. It leverages the RecipeKG knowledge graph, incorporating web scraping from allrecipes.com, unit normalization, and ingredient vectorization. The objectives encompass structured data creation, health score prediction using Classification and Regression techniques, and emphasizing ingredient amounts' significance. Results highlight the Histogram-Based Gradient Boosting model's performance, offering a valuable tool for informed dietary choices and open-source datasets for further research in online culinary diversity.

 
```


### Contributions 
We encourage the collaborative extention of our work. To simplify the process we monitor this repository's Issue tracker for requests of new terms/classes. We also check for reported errors or specific concerns related to the data.
