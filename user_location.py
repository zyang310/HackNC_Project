"""This program uses the ipstack api to access the user's location"""

import requests

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = '71225a217ee2a51d2f98059492bd18d5'

# Define the IP address you want to look up
ip_address = '152.23.233.51'

# Make the API request
response = requests.get(f'http://api.ipstack.com/{ip_address}?access_key={API_KEY}')

def function():
    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Access the location information
        city = data['city']
        country = data['country_name']
        latitude = data['latitude']
        longitude = data['longitude']


    else:
        # If the request was not successful, print an error message
        print(f'Error accessing the API. Status code: {response.status_code}')

    return city

print(function())


