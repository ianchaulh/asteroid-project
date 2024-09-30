import pandas as pd
import requests
from io import StringIO

'''
This script scrapes asteroid family data from the PDS (Planetary Data System) archive at 
https://sbnarchive.psi.edu/pds3/non_mission/EAR_A_VARGBDET_5_NESVORNYFAM_V3_0/data/families/.
'''

# CHANGE HERE
family = '010_2001uv209'

# URL to scrape
url = 'https://sbnarchive.psi.edu/pds3/non_mission/EAR_A_VARGBDET_5_NESVORNYFAM_V3_0/data/families/' + family + '.tab'

# Fetch the content from the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Read the content into a DataFrame
    column_names = [
        'Asteroid_ID', 'a', 'e', 'sin_i', 'H', 'C', 'Family_ID', 'Family_Number',
        'Family_Name'
    ]

    # Convert the content to a StringIO object for pandas
    data = StringIO(response.text)

    # Load the data into a DataFrame
    df = pd.read_csv(data, delim_whitespace=True, header=None, names=column_names)

    # Display the DataFrame
    print(df.head())

    # Optionally, save to a CSV file
    filename = family + '_data.csv'
    df.to_csv(filename, index=False)

    print(f"Data saved to {filename}.")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")