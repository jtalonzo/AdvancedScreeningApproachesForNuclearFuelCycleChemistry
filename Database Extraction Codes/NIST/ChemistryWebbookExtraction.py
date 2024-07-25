import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# NIST Chemistry WebBook URL database
BASE_URL = "https://webbook.nist.gov"
SEARCH_URL = "https://webbook.nist.gov/cgi/cbook.cgi"

# Extracting Chemical Data
def get_chemical_data(chemical name):
    params = {
        'Name': chemical_name,
        'Units' : 'SI'
    }
    response = requests.get(SEARCH_URL, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = {
        'Chemical Name': chemical_name,
        'Formula' : forumula,
        'CAS Registry Number": CAS_registry_number