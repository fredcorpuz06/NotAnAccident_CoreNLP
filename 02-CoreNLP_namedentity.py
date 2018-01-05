### Using Stanford CoreNLP for NIE and IE on articles
import pandas as pd
from nltk.tag.stanford import CoreNLPNERTagger
import requests
import re


date = '1228'
df = pd.read_csv('data/GDELT_query' + str(date) + '.csv')
wes_nlp = 'http://athina.wesleyan.edu:9000/'
	## Other python CoreMLP wrapper
# from pycorenlp import StanfordCoreNLP
# nlp = StanfordCoreNLP('http://localhost:9000')

##------------------------
## Named Entity Recognition
##-------------------------
	## Test for 1
# story_text = "Hartford, CT (AP) Police reported a major shoot-out between two teenagers yesterday. A 15-year-old boy fatally shot his 14-year-old friend."
# story_text = 'Rami Eid is studying at Stony Brook University in NY'
story_text = df['articles'][0]
ner = CoreNLPNERTagger(url=wes_nlp, encoding='utf8').tag(story_text.split()) 

	# Iterate through list
ner_clean = []
for item in ner:
	if item[1] != u'O':
		ner_clean.append(item)
print ner_clean

	## @param clean story text (unicode)
	## @return Named entity recognition 
def call_ner_clean(story_text):
	raw_ner = CoreNLPNERTagger(url=wes_nlp, encoding='utf8').tag(story_text.split()) 
	single_article = []
	for item in raw_ner:
		if item[1] != u'O':
			single_article.append(item)
	return single_article



  ## Create column of 'ner'
df['ners'] = df['articles'].apply(call_ner_clean)

def location_ner(clean_ner):
	locs = []
	for item in clean_ner:
		if item[1] == u'LOCATION':
			locs.append(item[0])
	return locs
    
df['locations'] = df['ners'].apply(location_ner)

date = 1228
df.to_csv('data/NER_query' + str(date) + '.csv')
print 'Successfully printed csv with NER_query'





