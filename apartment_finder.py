#!/home/john/MEGAsync/Projects/Webscrapers/Apartment_Finder/venv/bin/python3.11

import requests
from requests.exceptions import Timeout
import sys
import telegram_send
from bs4 import BeautifulSoup


# read apartments that have already been sent
known_apts = []
with open('known_apts.txt', 'r') as f:
	apts = f.readlines()
for apt in apts:
	apt = apt.rstrip('\n')
	known_apts.append(apt)


# data required for scraping
url = 'https://apartmentfinder.com'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
params = {
	'state': 'Louisiana',
	'city': 'Baton Rouge',
	'bedrooms': 2,
	'min_price': 850,
	'max_price': 1100
}

last_page = []

def scrape(page_num):
	# get html data for search results
	try:
		html = requests.get(f"{url}/{params['state'].replace(' ', '-')}/{params['city'].replace(' ', '-')}-Apartments/{params['bedrooms']}-Bedrooms/Page{page_num}/q/?nr={params['min_price']}&xr={params['max_price']}", headers=header, timeout=10)
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
		telegram_send.send(messages=[message], conf='jcc.config')
		telegram_send.send(messages=[message], conf='jvj.config')
	# scrape subsequent pages of search results
	if page_num + 1 > int(last_page[0]):
		sys.exit()
	scrape(page_num + 1)

scrape(1)


