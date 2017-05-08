import couchdb
from urllib2 import urlopen
import json
import requests
import traceback

# 20 keys
google_map_keys = ["AIzaSyAd-xrcEU7Na0p-kDy9_lPvBP9q2Jnna-c",
		"AIzaSyBCXQo12KuAOzL3Ksjt1i8TxdrJDrEPBvE",
		"AIzaSyCGWsGd97Xbp0dfVuMAwYvjQ2LIEvxLXXs",
		"AIzaSyASxKaE8x2uCocZbNm8HtMtVbxXLXHYUn8",
		"AIzaSyBLx39tWERh65fKTAdPcJ50znRJwELTob4",
		"AIzaSyCp8G1x6q8eDjlV5hpRZx8niKYXCfJBfok",
		"AIzaSyBGj7wIEJt9N7eWr8LI08uEhXmCmlGh7kk",
		"AIzaSyCYEXa33m9cSCbQP7YFyEDML4x9Qr9cixI",
		"AIzaSyBWvvoyjUMih-e7ZFX_8cBMKNSWUmA6dbQ",
		"AIzaSyC7n1egEvbh4u0hpSTxHCSezIYWgTa_VEc",
		"AIzaSyBCK6iSUsEoGGSKvfro254AmeDdci9O9nA",
		"AIzaSyBRdD6HuST3DivbEhcyIq0cVjq8UOIyu8E",
		"AIzaSyAyqF3y-N4py1egKp2UnBsJy3CnNSwZWec",
		"AIzaSyART7M5Q0kT85JHOpsjy1hrJQb7vJ5Yuuo",
		"AIzaSyBZd2pNTKxmbgph7U2-CEyEQWi5MMQqA08",
		"AIzaSyBNDJWy8M1DWAPeCHcdu28Ql1jHqKMOQrA",
		"AIzaSyDbRJW6xvL9e6OPVzsYVPDNuA7xMHP0TdE",
		"AIzaSyCfG13_SI-ltbvaVD0V8Ic3LHWe21lW0wc",
		"AIzaSyBmQMbvKpoNkaYEWJU18niAj1mxd7zn_4s",
		"AIzaSyBcb6u3lAI4a7kehIY6w5hOlLTrBzx-uew"]
		
count = 0

def getSuburb(lat, lon, key):
    url = "https://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&key=%s" % (lat, lon, key)
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
	try:
		if not response.text is None:

			result = json.loads(response.text.replace("Class\\", "Class"))
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
	except Exception as e:
		print("----------------text_sentiment_analysis----------------")
		print(e)
		print(response.text)
		traceback.print_exc()
		
def topic_extraction(txt):
	topics = set()
	
	url = "http://api.meaningcloud.com/topics-2.0"
	payload = "key=afaf04e25bc92f7d3981fbc4790fa05f&lang=en&txt=%s&tt=a" % {txt}
	headers = {'content-type': 'application/x-www-form-urlencoded'}
	response = requests.request("POST", url, data=payload, headers=headers)
	
	try:
		if not response.text is None:

			result = json.loads(response.text.replace("Class\\", "Class"))
			if result['status']['msg'] == 'OK':
				#parse entities
				entities = result['entity_list']
				for entity in entities:
					topics.add(entity['form'])
				#parse concepts:
				concepts = result['concept_list']
				for concept in concepts:
					topics.add(concept['form'])
	except Exception as e:
		print("---------------topic_extraction-----------------")
		print(e)
		print(response.text)
		traceback.print_exc()
	return list(topics)	

couch = couchdb.Server('http://admin:password@127.0.0.1:5984')
db = couch['tweets']

results = db.view('tweets_analysis/filter_tweets_with_coordinates_inside_melbourne', limit = 1000)
for row in results:
	###get Suburb
	coordinates = row.value[0]
	lon = coordinates[0]
	lat = coordinates[1]
	key = google_map_keys[count%20]
	try:
		suburb, state, country = getSuburb(lat, lon, key)
	except Exception as e:
		count = count +1
		key = google_map_keys[count%20]
		suburb, state, country = getSuburb(lat, lon, key)
	
	###sentiment analysis
	text = row.value[1]
	sentiment = text_sentiment_analysis(text)
	
	###topic extraction
	topics = topic_extraction(text)
	
	###update to add sentiment and suburb info into database
	doc_id = row.key
	doc = db.get(doc_id)
	doc['addressed'] = True
	doc['suburb'] = suburb
	doc['sentiment'] = sentiment
	doc['topics'] = topics
	db.save(doc)
print "finished"		