# coding: utf-8 -*-
### Learning How to Query from GDELT and Clean
import pandas as pd
import requests
from bs4 import BeautifulSoup
# import io
from unidecode import unidecode


##-------------
## Submit Query to GDELT
##-------------
url = 'https://api.gdeltproject.org/api/v2/doc/doc?query=(teen OR teenager OR child OR toddler OR boy OR girl OR "-year-old") (accidentally OR unintentionally) (shot OR killed OR wounded OR fired) (weapon OR gun OR shotgun OR rifle OR pistol) sourceCountry:US&mode=artlist&maxrecords=250&format=HTML&TIMESPAN=3d'

r = requests.get(url)

gdelt_html = r.text


soup = BeautifulSoup(gdelt_html, 'html.parser')

pretty_soup = soup.prettify()
	## Finding all hyperlinks and store into a list
a_tags = soup.find_all('a')
gdelt_links = []
gdelt_titles = []

for link in a_tags:
	gdelt_links.append(link.get('href'))
	gdelt_titles.append(link.text)
	

dict = {
	'links':gdelt_links,
	'titles': gdelt_titles
}

gdelt_df = pd.DataFrame(dict)
print 'Dim gdelt_df w/dups: ', 
print len(gdelt_df)

gdelt_df_nodups = gdelt_df.iloc[1::2] ## every link is repeated while title is given on odd indices
gdelt_df_nodups = gdelt_df_nodups.reset_index(drop=True)

print 'Dim gdelt_df w/o dups: ', 
print len(gdelt_df_nodups)


gdelt = gdelt_df_nodups
#print gdelt.head()

# df = df.dropna(axis=0, how='any')

# url_csv = 'https://api.gdeltproject.org/api/v2/doc/doc?query=(teen OR teenager OR child OR toddler OR boy OR girl OR "-year-old") (accidentally OR unintentionally) (shot OR killed OR wounded OR fired) (weapon OR gun OR shotgun OR rifle OR pistol) sourceCountry:US&mode=artlist&maxrecords=10&format=CSV&TIMESPAN=3d'
# r_csv = requests.get(url_csv)
# gdelt_csv = r.html
# df = pd.read_csv(io.StringIO(url_csv.decode('utf-8')))

##-----------------
## Keep only stories from TV Stations
##---------------
	## Pull out domain from the link
import re
	## want to make this everyting except ./
	## [^abc]	Find any character NOT between the brackets
pattern = r'[a-zA-Z0-9]*(?=.com|.net)' ## what site the link is from
gdelt['domain'] = gdelt['links'].apply(lambda x: re.findall(pattern, x)[0])

gdelt['domain'] = gdelt['domain'].str.upper()


stations =  pd.read_csv('market_station_info.csv')
is_tv = gdelt['domain'].isin(stations['UniqueIdentifier'])


tv_story = pd.merge(left=gdelt[is_tv], right=stations[['UniqueIdentifier', 'StationName','Location']],
	left_on='domain', right_on='UniqueIdentifier')
print '--------------------------'
print 'Cleaned GDELT query'
print tv_story.head()
print '-----------'

##------------------
## Download HTML content of page
##----------------
import readability as rd
	## Testing for 1
r = requests.get(tv_story['links'][2])
html = r.text
doc = rd.Document(html)
article = doc.summary()
soup = BeautifulSoup(article, 'html.parser')
uni = soup.get_text(strip=True)
cleaner = unidecode(uni)
print cleaner
# cleaner= clean.decode('unicode_escape').encode('ascii','ignore')

	## @param URL
	## @return: The text of the main paragraph of the article
def store_pretty(url):
	r = requests.get(url)
	html = r.text
	doc = rd.Document(html)
	article = doc.summary()
	soup = BeautifulSoup(article, 'html.parser')
	uni = soup.get_text(strip=True)
	cleaner = unidecode(uni)
	return cleaner



	## Get text from URL
tv_story['articles'] = tv_story['links'].apply(store_pretty)

# date = '1228'
# tv_story.to_csv('GDELT_query' + str(date) + '.csv', encoding='utf-8')
