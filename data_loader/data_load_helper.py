import pandas as pd 
import numpy as np 
import requests 
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
import pickle
import json
import xml.etree.ElementTree as ET


class DataLoader():
    def __init__(self): 
        self.data_source = ""
    
    def load_excel_file(self, filename):
        try:
            data = pd.read_excel(filename) 
            return data
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return None
    
    def load_json_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return None
        except json.JSONDecodeError:
            print(f"Failed to decode JSON data from file '{filename}'.")
            return None
    def load_sas7bdat_file(self, filename):
        try:
            df = pd.read_sas(filename)
            return df
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred while reading '{filename}': {e}")
            return None
    def load_xml_file(self, filename):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            return root
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return None
        except ET.ParseError as e:
            print(f"Error parsing XML file '{filename}': {e}")
            return None