import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Define paths
data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')

# Choose network
network = 'songbird' # 'flare'

# Data saving paths

txt_file_path = os.path.join(data_folder, f'{network}_ftso.txt')
csv_file_path = os.path.join(data_folder, f'{network}_ftso_df.csv')

# Create data folder if it doesn't exist
os.makedirs(data_folder, exist_ok=True)

# URL of the validators page
if network == 'flare':
    url = "https://flaremetrics.io"
else:
    url = "https://flaremetrics.io/songbird"

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
    ftsos = soup.find_all("tr", class_="h-12 border-y border-gray-100 dark:border-gray-600 text-sm font-medium md:hover:bg-gray-50 md:dark:hover:bg-gray-700")  # Adjust the class name if necessary

    # Initialize lists to store the data
    names = []
    active_vote_powers = []
    locked_vote_powers = []
    locked_vote_power_percentages = []
    active_vote_power_percentages = []
    reward_rates = []
    IQR_rates_6h = []
    elastic_rates_6h = []
    availabilities = []
    fees = []

    for ftso in ftsos:
        # right text
        right_texts = ftso.find_all("td", class_="text-right")
        # Extract FTSO name
        name = ftso.find("a", class_="hover:text-indigo-600 dark:hover:text-indigo-300").get_text(strip=True)
        names.append(name)
        
        # Extract FTSO vote power 
        active_vote_power = right_texts[0].find("div").get_text(strip=True).replace(",",'')
        locked_vote_power = ftso.find("div", class_="text-gray-400 font-normal text-sub").find("span", class_="cursor-help z-0").get_text(strip=True).replace(",",'')

        active_vote_powers.append(active_vote_power)
        locked_vote_powers.append(active_vote_power)

        # Extract vp %
        active_vote_power_percentage = ftso.find("div", class_="w-12").find("div").get_text(strip=True).replace("%",'')
        locked_vote_power_percentage = ftso.find("div", class_="flex items-center justify-end gap-4").find("div", class_="text-gray-400 font-normal text-sub").find("span", class_="cursor-help z-0").get_text(strip=True).replace("%",'')

        active_vote_power_percentages.append(active_vote_power_percentage)
        locked_vote_power_percentages.append(locked_vote_power_percentage)

        # Extract reward rates
        reward_rate = right_texts[2].find("div").get_text(strip=True)
        IQR_rate_6h = right_texts[3].get_text(strip=True).replace("%", '')
        elastic_rate_6h = right_texts[4].get_text(strip=True).replace("%", '')

        reward_rates.append(reward_rate)
        IQR_rates_6h.append(IQR_rate_6h)
        elastic_rates_6h.append(elastic_rate_6h)

        # Extract availability
        availability = ftso.find("div", class_="flex items-center justify-end font-normal").get_text(strip=True).replace("%", '')

        availabilities.append(availability)

        # Extract FTSO fee
        fee = ftso.find("td", class_="pr-2 text-right").find("div", class_="flex justify-end gap-2").find("span").get_text(strip=True).replace("%", '')
        fees.append(fee)
        
    data = {
        "Name": names,
        "Active vote power": active_vote_powers,
        "Locked vote power": locked_vote_powers,
        "Active vp %": active_vote_power_percentages,
        "Locked vp %": locked_vote_power_percentages,
        "Reward rate": reward_rates,
        "IQR rate 6h %": IQR_rates_6h,
        "Elastic rate 6h %": elastic_rates_6h,
        "Availability": availabilities,
        "Fee": fees
    }
    
    flare_metrics_df = pd.DataFrame(data)
    
    # Save DataFrame to a CSV file
    flare_metrics_df.to_csv(csv_file_path, index=False)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
