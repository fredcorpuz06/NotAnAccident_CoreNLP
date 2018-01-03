### Using CoreNLP for Information extraction

##---------------
## Example Get Request
##-------------------
'''
r = requests.get('https://api.github.com/events') ## response object 'r'
r = requests.get('http://example.com')
print r.encoding ## guessed the encoding as 'utf-8'
print r.content ## use this to find the encoding
r.encoding = 'ISO-8859-1' ## set the encoding
print r.text
print r.status_code
print r.json()
	
	# Passing parameters: ?key=val
payload = {'key1': 'value1','key2': ['value2', 'value3']}

r = requests.get('http://httpbin.org/get', params=payload)
print r.url ## http://httpbin.org/get?key1=value1&key2=value2&key2=value3


headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
'''
##------------------
## Example Post Request
##----------------
'''
payload = {'key1': 'value1','key2': ['value2', 'value3']} ## as dict
payload = [('key1', 'value1'), ('key2', 'value2'), ('key2', 'value3')] ## as list of tuples
r = requests.post('http://httpbin.org/post', data=payload)

url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'}} ## send multi-part files
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')} ## Send strings as files

r = requests.post(url, files=files)

print r.text
'''


# 	## Define API-endpoint
# API_ENDPOINT = 'http://pastebin.com/api/api_post.php'

# API_KEY = 'XXXXXXXXXXXXXXXXX'

# 	## Source code
# source_code = '''
# print('Hello, world!')
# a = 1
# b = 2 
# print a + b
# '''
# 	## Data to be sent to API
# data = {'api_dev_key': API_KEY,
# 		'api_option': 'paste',
# 		'api_paste_code': source_code,
# 		'api_paste_format': 'python'}

# 	## Sending post request and savinng response as response object
# r = requests.post(url=API_ENDPOINT, data=data)

# 	## Extracting response text
# pastebin_url = r.text
# print "The pastebin URL is:%s" % pastebin_url

##-----------------
## Sending a Post Request
##---------------------
import pandas as pd
from nltk.tag.stanford import CoreNLPNERTagger
import requests
import re

date = '1228'
df = pd.read_csv('P:\QAC\Projects\datadive17\NotAnAccident\Fred_files\GDELT_query' + str(date) + '.csv')
wes_nlp = 'http://athina.wesleyan.edu:9000/'
	## Create a CSV of articles texts to send as data in POST
article_text = df.iloc[:, -1]
dict_articles = article_text.to_dict()

single_article = dict_articles[0]


r = requests.post(wes_nlp, data=single_article)
print r.url
print r.status_code

r_dic = r.json()



# ner = r_dic['sentences'][1]['entitymentions'] ## list
# for item in ner:
# 	print ''