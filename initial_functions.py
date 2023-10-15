
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd



# the function that obtain urls of recipes from json files
def scrap_url(jsonfiles):
    # Initialize an empty list to store the collected URLs
    collected_urls = []

    for rec in jsonfiles:
        # Iterate through the JSON files in the directory
        for filename in os.listdir(rec):
            if filename.endswith('.json'):
                
                # Construct the full path to the JSON file
                file_path = os.path.join(rec, filename)
                

                # Load the JSON data from the file
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)

                    # Extract the URL from the "mainEntityOfPage" field
                    if 'mainEntityOfPage' in data[1]:
                        
                        url = data[1]['mainEntityOfPage']
                        collected_urls.append(url)
    #delete duplicates
    collected_urls=list(set(collected_urls))
    return collected_urls



# the function scrapes servings per recipe from allrecipes.com and creates a df
def serve_amount(recipe_urls):
    # Initialize an empty DataFrame
    data = {'URL': [], 'Servings': []}
    df = pd.DataFrame(data)

    # Iterate over the URLs
    for url in recipe_urls:
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the specific element that contains servings information (modify this based on the actual HTML structure)
            servings_element = soup.find('th', class_='mntl-nutrition-facts-label__table-head-subtitle')
            servings_span = servings_element.find_all('span', recursive=False)[1]
            servings_value = servings_span.get_text() if servings_span else 'N/A'
            

            # Add the URL and servings information to the DataFrame
            df = df.append({'URL': url, 'Servings': servings_value}, ignore_index=True)
        except Exception as e:
            # Handle any errors or exceptions that may occur during scraping
            df=df.append({'URL': url, 'Servings': 'url error'}, ignore_index=True)
    return df

