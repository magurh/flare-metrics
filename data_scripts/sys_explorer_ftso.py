"""
A script for web scrapping ftso data from the Flare Systems Explorer, currently only available for Songbird: https://songbird-systems-explorer.flare.rocks/entities/ftsoDataProvider
"""

import os
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

from config import DATA_PATH


# Data saving paths
json_file_path = os.path.join(DATA_PATH, 'sys-explorer_sgb_ftso.json')
csv_file_path = os.path.join(DATA_PATH, 'sys-explorer_sgb_ftso.csv')

# Create data folder if it doesn't exist
os.makedirs(DATA_PATH, exist_ok=True)

url = 'https://songbird-systems-explorer.flare.rocks/backend-url/api/v0/entity/ftso?limit=100&offset=0&sort_ascending=false&sort_by=registration_weight&query='

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON content
    data = response.json()
    
    # Save the JSON data to a file
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        
     # Extract relevant information and create a list of dictionaries
    records = []
    for item in data['results']:
        record = {
            'Name': item['display_name'],
            'Address': item['identity_address']['address'],
            'Active': item['providersuccessrate']['active'],
            'Registration_weight': item['providersuccessrate']['registration_weight'],
            'Primary (%)': int(item['providersuccessrate']['primary_bips']) / 100,
            'Secondary (%)': int(item['providersuccessrate']['secondary_bips']) / 100,
            'Availability (%)': int(item['providersuccessrate']['availability_bips']) / 100,
            'Total reward': item['rewards']['total_reward'],
            'Current earnings': item['rewards']['current_earnings'],
            'Reward rate': item['rewards']['reward_rate'],
        }
        records.append(record)
    
    # Convert the list of dictionaries into a DataFrame
    ftso_df = pd.DataFrame(records)

    ftso_df['Registration_weight'] = ftso_df['Registration_weight'].fillna(0).astype(float)/10**18
    ftso_df['Total reward'] = ftso_df['Total reward'].fillna(0).astype(float)/10**18
    ftso_df['Current earnings'] = ftso_df['Current earnings'].fillna(0).astype(float)/10**18
    ftso_df['Reward rate'] = ftso_df['Reward rate'].fillna(0).astype(float)
    
    
    # Optionally, save to a CSV file
    ftso_df.to_csv(csv_file_path, index=False)
    
else:
    print("Failed to retrieve data. Status code:", response.status_code)