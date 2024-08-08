"""
A script for web scrapping ftso data from flaremetrics.io.
Before running, make sure to select the appropriate network (flare or songbird), by setting the network parameter below.
"""

import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

from config import DATA_PATH

# Define paths
txt_file_path = os.path.join(DATA_PATH, 'flare-metrics_flr_validators.txt')
csv_file_path = os.path.join(DATA_PATH, 'flare-metrics_flr_validators.csv')

# Create data folder if it doesn't exist
os.makedirs(DATA_PATH, exist_ok=True)

# URL of the validators page
url = "https://flaremetrics.io/validators"

# Send a GET request to the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.content, "html.parser")

    # Save soup as a text file
    with open(txt_file_path, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    
    # Find all validator entries
    validators = soup.find_all("tr", class_="h-16 border-y border-gray-100 dark:border-gray-600 text-sm font-medium md:hover:bg-gray-50 md:dark:hover:bg-gray-700")  # Adjust the class name if necessary
    
    # Initialize lists to store the data
    addresses = []
    names = []
    uptimes = []
    fees = []
    delegators = []
    owner_stakes = []
    delegators_stakes = []
    free_spaces = []
    total_stakes = []
    
    for validator in validators:
        # Extract validator address
        address = validator.find("div", class_="text-ellipsis overflow-hidden text-xs opacity-70").get_text(strip=True)
        addresses.append(address)

        # Extract registered name
        name = validator.find("div", class_="flex items-center gap-x-2 font-semibold").get_text(strip=True)
        names.append(name)
        
        # Extract validator uptime
        uptime = validator.find("td", class_="text-left font-light pr-2").get_text(strip=True)
        uptime = uptime.replace('%', '')
        uptimes.append(uptime)
        
        # Extract total stake
        total_stake = validator.find("td", class_="text-left font-light").get_text(strip=True).split(":")[0][:-8]
        total_stake = total_stake.replace(',', '')
        total_stakes.append(total_stake)
        
        # Extract owner stake
        owner_stake = validator.find("div", string="Owner:").find_next("div", class_="text-right").get_text(strip=True).split()[0][:-3]
        owner_stake = owner_stake.replace(',', '')
        owner_stakes.append(owner_stake)
        
        # Extract delegators stake
        delegators_stake = validator.find("div", string="Delegators:").find_next("div", class_="text-right").get_text(strip=True).split()[0][:-3]
        delegators_stake = delegators_stake.replace(',', '')
        delegators_stakes.append(delegators_stake)
        
        # Extract free space
        free_space = validator.find("div", string="Free Space:").find_next("div", class_="text-right").get_text(strip=True).split()[0][:-3]
        free_space = free_space.replace(',', '')
        free_spaces.append(free_space)

        # Extract number of delegators
        delegators_count = validator.find("td", class_="relative text-left font-light").get_text(strip=True).split("This validator will not earn rewards for itself or its delegators as it either does not run an FTSO data provider or it is underperforming.")[0]
        delegators_count = delegators_count.replace(',', '')
        delegators.append(delegators_count)

        # Extract fee
        fee = validator.find_all("td", class_="text-left font-light")[1].get_text(strip=True)[:-1]
        fees.append(fee)
    
    # Create a DataFrame
    data = {
        'Address': addresses,
        'Name': names,
        'Total Stake': total_stakes,
        'Owner Stake': owner_stakes,
        'Delegators Stake': delegators_stakes,
        'Free Space': free_spaces,
        'Delegators': delegators,
        'Uptime %': uptimes,
        'Fee %': fees
    }
    
    flare_metrics_df = pd.DataFrame(data)
    
    # Save DataFrame to a CSV file
    flare_metrics_df.to_csv(csv_file_path, index=False)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
