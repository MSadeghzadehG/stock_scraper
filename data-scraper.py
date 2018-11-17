import requests
import os
from lxml import html
import json
import numpy as np
from time import sleep
from selenium import webdriver


def find_elements_by_xpath(text, xpath):
    tree = html.fromstring(text)
    list = []
    for link in tree.xpath(xpath):
        list.append(link)
    return list

naghshe_bazzar_url = 'http://www.tsetmc.com/Loader.aspx?ParTree=15131F#'
# browser = webdriver.Firefox() #replace with .Firefox(), or with the browser of your choice
# browser.get(naghshe_bazzar_url) #navigate to the page


# main = browser.find_element_by_id("main")
# all_stocks = browser.find_element_by_class_name('{c}')

f = open('MarketWatch.htm', 'r')
all_stocks = find_elements_by_xpath(f.read(), '//*[@id="main"]/div')
f.close()
# print(len(all_stocks))
ids = []
for div in all_stocks:
    if (div.attrib['class']=='{c}'):
        ids.append(div.attrib['id'])
        # print(type(div.iter().next()))

get_data_url = 'http://tsetmc.ir/tsev2/data/Export-txt.aspx?t=i&a=1&b=0&i='
if not os.path.exists('./data/'):
        os.makedirs('./data/')
for id in ids:
    request = requests.get(get_data_url+id)
    try:
        name = str(request.text).splitlines()[1].split(',')[0]
        print(name + ' done')
        f = open('./data/'+name+'.csv', 'w')
        f.write(request.text)
        f.close()
    except:
        pass