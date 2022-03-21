# importing modules
import requests
from bs4 import BeautifulSoup

# URL for scrapping data
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

# get URL html
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = []

# soup.find_all('td') will scrape every
# element in the url's table
data_iterator = iter(soup.find_all('td'))

# data_iterator is the iterator of the table
# This loop will keep repeating till there is
# data available in the iterator
while True:
	try:
		country = next(data_iterator).text
		confirmed = next(data_iterator).text
		deaths = next(data_iterator).text
		continent = next(data_iterator).text

		# For 'confirmed' and 'deaths',
		# make sure to remove the commas
		# and convert to int
		data.append((
			country,
			int(confirmed.replace(',', '')),
			int(deaths.replace(',', '')),
			continent
		))

	# StopIteration error is raised when
	# there are no more elements left to
	# iterate through
	except StopIteration:
		break

# Sort the data by the number of confirmed cases
data.sort(key=lambda row: row[1], reverse=True)

for item in data:
	print(item)
	for i in item:
		print(i)

