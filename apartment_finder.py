#!/usr/bin/env python3

import requests
from requests.exceptions import Timeout
import sys
import os
import telegram_send
from bs4 import BeautifulSoup
from dotenv import load_dotenv


# load parameters from .env
load_dotenv()
state = os.getenv('STATE')
city = os.getenv('CITY')
bedrooms = os.getenv('BEDROOMS')
min_price = os.getenv('MIN_PRICE')
max_price = os.getenv('MAX_PRICE')
pets = os.getenv('PETS')
filters = os.getenv('FILTERS')
spec = os.getenv('SPECIALTIES')
rating = os.getenv('MIN_RATING')
keywords = os.getenv('KEYWORDS')

# load telegram configurations
if os.path.isfile('configs.txt') == False:
	print('You have not configured a bot. Please run configure.py')
	sys.exit()
with open('configs.txt', 'r') as f:
	configs = f.readlines()

# read apartments that have already been sent
known_apts = []
if os.path.isfile('known_apts.txt') == False:
	open('known_apts.txt', 'w').close()
with open('known_apts.txt', 'r') as f:
	apts = f.readlines()
for apt in apts:
	apt = apt.rstrip('\n')
	known_apts.append(apt)


# data required for scraping
url = 'https://apartmentfinder.com'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
params = {
	'state': state.replace(' ', '-'),
	'city': city.replace(' ', '-'),
	'bedrooms': bedrooms,
	'min_price': min_price,
	'max_price': max_price,
	'pets': pets,
	'filters': filters,
	'spec': spec,
	'rating': rating,
	'keywords': keywords.replace(' ', '+').split(',')
}
keywords = '%2C'.join(params['keywords'])


# scrape the website
last_page = []
def scrape(page_num):
	# get html data for search results
	try:
		html = requests.get(f"{url}/{params['state'].replace(' ', '-')}/{params['city'].replace(' ', '-')}-Apartments/{params['bedrooms']}-Bedrooms/Page{page_num}/q/?nr={params['min_price']}&xr={params['max_price']}&pt={params['pets']}&sp={params['spec']}&am={params['filters']}&kd={keywords}&ra={params['rating']}&", headers=header, timeout=10)
	except Timeout:
		print('Request timed out.')
		sys.exit(1)

	# parse html to get name of apartment and link to it
	soup = BeautifulSoup(html.text, 'html.parser')

	# find last page of results
	if page_num == 1:
		page_range = soup.find('span', class_='pageRange')
		last_page.append(page_range.text.split('Page 1 of ')[1])

	for item in soup.select('h2 > a'):
		if item['title'] in known_apts:
			continue
		message = f"{item['title']}: {item['href']}"
		with open('known_apts.txt', 'a') as f:
			f.write(f"{item['title']}\n")
		for config in configs:
			telegram_send.send(messages=[message], conf=config.rstrip('\n'))
	# scrape subsequent pages of search results
	if page_num + 1 > int(last_page[0]):
		sys.exit()
	scrape(page_num + 1)

scrape(1)


