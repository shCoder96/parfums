#!/usr/bin/env python

from sys import *
from requests import *
from bs4 import *

brand_links = []
brand_model = {}

target = get('https://www.parfumerovv.ru/brands').text

soup_target_brand = BeautifulSoup(target)
target_link_brand = soup_target_brand.findAll('a', class_='bg_item_text')

for link in target_link_brand:
    brand_links.append(link)
print(len(brand_links))

for brand in brand_links:
    get_page_status = get(f'https://www.parfumerovv.ru/{brand.text}')
    get_page_status = get_page_status.content.decode('utf-8')
    print(f'{get_page_status.url} \t --------- \t --------- \t ------> {get_page_status.status_code}')
    if get_page_status.status_code == 404:
        brand_links.remove(brand)
    with open('valid_link.txt', 'w') as line:
        print(brand)

print(len(brand_links))

