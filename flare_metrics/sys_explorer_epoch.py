"""
A script for web scrapping ftso data from the Flare Systems Explorer, currently only available for Songbird: https://songbird-systems-explorer.flare.rocks
"""

import os
import requests
import json
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import argparse

from flare_metrics.config import DATA_PATH


def collect_epoch_data(reward_epoch_id):
    # Data saving paths
    # json_file_path = os.path.join(DATA_PATH, f'sys-explorer_sgb_epoch_{reward_epoch_id}.json')
    csv_file_path = os.path.join(DATA_PATH, f'sys-explorer_sgb_epoch_{reward_epoch_id}.csv')

    # Create data folder if it doesn't exist
    os.makedirs(DATA_PATH, exist_ok=True)

    url = f'https://songbird-systems-explorer.flare.rocks/backend-url/api/v0/reward_epoch/registered_voters?reward_epoch_id={reward_epoch_id}&limit=100&offset=0'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON content
        data = response.json()

        # Extract relevant information and create a list of dictionaries
        records = []
        for item in data['results']:
            record = {
                'Name': item['display_name'],
                'Address': item['identity_address']['address'],
                'FastUpdates Registration': item['voter_registered']['public_key'],
                'Normalised weight': int(item['normalised_weight']),
                'Registration weight': float(item['voter_registered']['registration_weight']),
                'Registration block': int(item['voter_registered']['block']),
                'Delegation weight': float(item['voter_registration_info']['w_nat_weight']),
                'Capped delegation weight': float(item['voter_registration_info']['w_nat_capped_weight']),
            }
            records.append(record)

        # Convert the list of dictionaries into a DataFrame
        ftso_df = pd.DataFrame(records)

        # Process the data
        ftso_df['Delegation weight'] = ftso_df['Delegation weight'].fillna(0) / 10**18
        ftso_df['Capped delegation weight'] = ftso_df['Capped delegation weight'].fillna(0) / 10**18
        ftso_df['FastUpdates Registration'] = np.where(ftso_df['FastUpdates Registration'] == '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', 0, 1)

        # Optionally, save to a CSV file
        ftso_df.to_csv(csv_file_path, index=False)

        print(f"Data successfully saved to {csv_file_path}.")

    else:
        print("Failed to retrieve data. Status code:", response.status_code)


def main():
    parser = argparse.ArgumentParser(description='Collect epoch data from the Songbird Systems Explorer.')
    parser.add_argument('reward_epoch_id', type=int, help='The reward epoch ID to collect data for.')

    args = parser.parse_args()
    collect_epoch_data(args.reward_epoch_id)