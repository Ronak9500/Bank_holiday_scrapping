import pandas as pd
import numpy
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup,Comment
import re
import requests
from urllib import request
from pprint import pprint

url='https://www.edudwar.com/andhra-pradesh-holidays-list/' # change the link as per the state wise

data=requests.get(url)

my_data=[]
html=BeautifulSoup(data.text,'html.parser')

data=html.find('table')