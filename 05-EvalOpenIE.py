### Parse through OpenIE results
import pandas as pd
import requests
# from CoreNLP_infoextraction import openie_post_extract

df = pd.read_pickle('OpenIE.pkl')

article1 = df['articles'][2]
wes_nlp = 'http://athina.wesleyan.edu:9000/'
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
			su = triple['subject'] , triple['relation'] , triple['object']
			summaries.append(su)
	return summaries

ie = openie_post_extract(article1)

# r = requests.post(wes_nlp, data=article1)
# print r.status_code
# r_dic = r.json()
print '------------Article--------------------'
print article1
print '------OpenIE Triples (subject, relation, object)--------'
def l_tup_print(openie_tuple):
	assert openie_tuple != []
	for item in openie_tuple:
		print item[0], ';', item[1], ';', item[2]
l_tup_print(ie)