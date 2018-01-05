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
df = pd.read_csv('data/GDELT_query' + str(date) + '.csv')
wes_nlp = 'http://athina.wesleyan.edu:9000/'

'''
	## Create a dict of articles texts to send as data in POST
article_text = df.iloc[:, -1]
dict_articles = article_text.to_dict()

single_article = dict_articles[0]
single_article2 = dict_articles[2]

r = requests.post(wes_nlp, data=single_article)
# print r.url
print r.status_code

# r_many = requests.post(wes_nlp, data=dict_articles)
# print r_many.status_code

r2 = requests.post(wes_nlp, data=single_article2)
# print r.url
print r2.status_code

r_dic = r.json()
r2_dic = r2.json()
r_dic.keys() ## Dict: [u'corefs', u'sentences']
len(r_dic['sentences']) ## List: 3
r_dic['sentences'][0].keys() ## Dict: [u'openie', u'index', u'enhancedDependencies', u'basicDependencies', u'parse', u'tokens', u'entitymentions', u'enhancedPlusPlusDependencies', u'kbp']
len(r_dic['sentences'][0]['openie']) ## List: 1 (**list of dictionaries)
r_dic['sentences'][0]['openie'][0].keys() ## Dict: [u'subjectSpan', u'relationSpan', u'objectSpan', u'object', u'relation', u'subject']

# triples = r2_dic['sentences'][0]['openie']
r_dic['sentences'][1]['openie']
r_dic['sentences'][2]['openie']

sentences = r2_dic['sentences']
# print triple['object'], ';', triple['relation'], ';', triple['subject']
'''

	## @params: Article_text is mostly ASCII format
	## @return: List of Triples [('object1', 'relation1', 'triple1'),('object2', 'relation2', 'triple2') ]
def openie_post_extract(article_text):
	r = requests.post(wes_nlp, data=article_text)
	print r.status_code
	if r.status_code != 200:
		return []
	r_dic = r.json()
	summaries = []
	sentences = r_dic['sentences']
	for sentence in sentences:
		triples = sentence['openie']
		for triple in triples:
			# print triple['object'], ';', triple['relation'], ';', triple['subject']
			su = triple['object'] , triple['relation'] , triple['subject']
			summaries.append(su)
	return summaries

# print '-------------------'
# r_sum = openie_extract(r_dic)
# print '-----------------'
# r2_sum = openie_extract(r2_dic)

df['openie_tuples'] = df['articles'].apply(openie_post_extract)
	
	## @params: list of tuples
	## @action: print
def l_tup_print(openie_tuple):
	assert openie_tuple != []
	for item in openie_tuple:
		print item[0], ';', item[1], ';', item[2]

	## Test print
l_tup_print(df['openie_tuples'][3])


df.to_csv('data/OpenIE_query' + str(date) + '.csv')
# df.to_pickle('data/OpenIE_query' + str(date) + '.pkl')
print 'Succesfully got OpenIE of articles and print to CSV'