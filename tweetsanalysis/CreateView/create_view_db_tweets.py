#This program is used to create views for DB Tweets

import couchdb
from urllib2 import urlopen
import json
import requests

def getSuburb(lat, lon):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&sensor=false" % (lat, lon)
    v = urlopen(url).read()
    j = json.loads(v)
    components = j['results'][0]['address_components']
    country = state = suburb = None
    for c in components:
    	if "country" in c['types']:
    		country = c['long_name']
    	if "administrative_area_level_1" in c['types']:
    		state = c['long_name']
    	if "locality" in c['types']:
    		suburb = c['long_name']
    return suburb, state, country
	
def text_sentiment_analysis(text):
	url = "http://api.meaningcloud.com/sentiment-2.1"
	payload = "key=afaf04e25bc92f7d3981fbc4790fa05f&lang=en&txt=%s&model=general" % {text}
	headers = {'content-type': 'application/x-www-form-urlencoded'}
	
	response = requests.request("POST", url, data=payload, headers=headers)
	
	if not response.text is None:
		result = json.loads(response.text)
		if result['status']['msg'] == 'OK':
			score_tag = result['score_tag']
			positive_result = ['P+', 'P']
			negative_result = ['N+', 'N']
			neutral_result = ['NEU', 'NONE']
			if score_tag in positive_result:
				return 'positive'
			elif score_tag in negative_result:
				return 'negative'
			else:
				return 'neutral'
		
def topic_extraction(txt):
	topics = set()
	
	url = "http://api.meaningcloud.com/topics-2.0"
	payload = "key=afaf04e25bc92f7d3981fbc4790fa05f&lang=en&txt=%s&tt=a" % {txt}
	headers = {'content-type': 'application/x-www-form-urlencoded'}
	response = requests.request("POST", url, data=payload, headers=headers)
	
	if not response.text is None:
		result = json.loads(response.text)
		if result['status']['msg'] == 'OK':
			#parse entities
			entities = result['entity_list']
			for entity in entities:
				topics.add(entity['form'])
			#parse concepts:
			concepts = result['concept_list']
			for concept in concepts:
				topics.add(concept['form'])
	return list(topics)	


with open('./MapReduceFunctions/filter_tweets_with_coordinates_inside_melbourne.js') as f:
	within_melb_map = f.read()

with open('./MapReduceFunctions/sentiment_summary_map.js') as f:
	sentiment_map = f.read()

with open('./MapReduceFunctions/sentiment_summary_reduce.js') as f:
	sentiment_reduce = f.read()

with open('./MapReduceFunctions/filter_tweets_with_tump.js') as f:
	filter_tweets_with_tump = f.read()	

with open('./MapReduceFunctions/tweets_with_vulgar_word.js') as f:
	tweets_with_vulgar_word = f.read()	

design_doc = {
  "_id": "_design/tweets_analysis",
  "language": "javascript",
  "views": {
    "filter_tweets_with_coordinates_inside_melbourne": {
      	"map": within_melb_map
    },
    "sentiment_summary": {
    	"map": sentiment_map,
    	"reduce": sentiment_reduce
    },
    "filter_tweets_with_tump":{
    	"map": filter_tweets_with_tump
    },
    "tweets_with_vulgar_word":{
    	"map": tweets_with_vulgar_word
    }
  }
}

couch = couchdb.Server()
db = couch['tweets']

db.save(design_doc)

results = db.view('tweets_analysis/filter_tweets_with_coordinates_inside_melbourne')
print len(results)
for row in results:
	#get Suburb
	coordinates = row.value.get('coordinates').get('coordinates')
	lon = coordinates[0]
	lat = coordinates[1]
	suburb, state, country = getSuburb(lat, lon)
	
	#sentiment analysis
	text = row.value.get('text')
	sentiment = text_sentiment_analysis(text)
	
	#topic extraction
	topics = topic_extraction(text)
	
	#update to add sentiment and suburb info into database
	doc_id = row.key
	doc = db.get(doc_id)
	doc['addressed'] = True
	doc['suburb'] = suburb
	doc['sentiment'] = sentiment
	doc['topics'] = topics
	db.save(doc)
	
	
results = db.view('tweets_analysis/sentiment_summary', reduce = True, group_level = 2)
print len(results)
for row in results:
	print row.key
	print row.value




