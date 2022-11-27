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

headers=[]

for i in data.findAll('tr'):
    title=i.text
    headers.append(title)
    
festival = []
date = []
day = []
for i in headers[1:]:
    temp = i.split("\n")
    festival.append(temp[1])
    date.append(temp[2])
    day.append(temp[3])
    
ap=pd.DataFrame({"festival":festival,'date':date,"day":day})

url='https://housing.com/news/bank-holiday-list/'
data=requests.get(url)
my_data=[]
html=BeautifulSoup(data.text,'html.parser')
data=html.find_all('table')
second_table=data[-1]
headers=[]

for i in second_table.findAll('tr'):
    title=i.text
    headers.append(title)

holiday = []
date = []

for i in headers[1:]:
    temp = i.split("\n")
    holiday.append(temp[1])
    date.append(temp[2])
   
sat_holiday=pd.DataFrame({"holiday":holiday,'date':date})