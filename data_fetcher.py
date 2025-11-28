from dotenv import load_dotenv
import os
import requests
load_dotenv()
API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name):
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    response = requests.get(url, headers={"X-Api-Key": API_KEY})
    data = response.json()
    if not data:
        return f"The animal {animal_name} doesn't exist."
    return data




