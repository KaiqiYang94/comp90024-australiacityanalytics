import couchdb
from urllib2 import urlopen
import json
import requests
import traceback
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

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

meaningcloud_keys=["afaf04e25bc92f7d3981fbc4790fa05f",
		"24d637371d7361126017306a854a5fb3",
		"9a92b9afa6ea4dc0dddc7139e446c2f2",
		"4223e7a9714645c6f2bab8f489101534",
		"df196af806319c62c4d8e3cf8b9b8a32",
		"1ca99d6ee86674ff760edcc27d0c396e",
		"2513eab559e8f00fe555587c7fcf7e33",
		"4798949c53da78ca3778b0c075f407bd",
		"eb127df802db36b5ad36717482ea9b54",
		"cd82aa3c3c0e4eb8c4e65f5135f0148c",
		"16e45143d271828a776c57a2aa6131ee",
		"53d91ded21179441115c495bbcf20b37",
		"3540b6de695ce61ed531958631f39349",
		"e24a9cbd480d755d22724cd8ea264222",
		"1fab188d05d431540f52cebdc06c9bfe",
		"24ba8e6db4b406210a2c69aaddd6a989",
		"ac836a76eb70944ed1faf9b43f90dfcd",
		"5ac94e9c00bb632ce6be5920493e6cd1",
		"7656812a83a147bd09863e78836fbb9a"]		
google_count = 0
meaningcloud_count = 0
meaningcloud_len = len(meaningcloud_keys)
google_len = len(google_map_keys)

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
	
def text_sentiment_analysis(text, key):
	url = "http://api.meaningcloud.com/sentiment-2.1"
	payload = "key=%s&lang=en&txt=%s&model=general" % (key, text)
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
		
def topic_extraction(txt, key):
	topics = set()
	
	url = "http://api.meaningcloud.com/topics-2.0"
	payload = "key=%s&lang=en&txt=%s&tt=a" % (key, txt)
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

def meaningcloud_utilization(text):
	while meaningcloud_count < meaningcloud_len:
		key = meaningcloud_keys[meaningcloud_count]
		try:
			sentiment = text_sentiment_analysis(text, key)
			topics = topic_extraction(text, key)
			return sentiment, topics
		except:
			meaningcloud_count = meaningcloud_count + 1
	exit()

couch = couchdb.Server('http://admin:password@127.0.0.1:5984')
db = couch['tweets']

results = db.view('tweets_analysis/filter_tweets_with_coordinates_inside_melbourne', limit = 1000)
for row in results:
	###get Suburb
	coordinates = row.value[0]
	lon = coordinates[0]
	lat = coordinates[1]
	key = google_map_keys[google_count%google_len]
	try:
		suburb, state, country = getSuburb(lat, lon, key)
	except Exception as e:
		google_count = google_count +1
		key = google_map_keys[google_count%google_len]
		suburb, state, country = getSuburb(lat, lon, key)
	
	###sentiment analysis and topic extraction
	text = row.value[1]	
	sentiment, topics = meaningcloud_utilization(text)
	
	###update to add sentiment and suburb info into database
	doc_id = row.key
	doc = db.get(doc_id)
	doc['addressed'] = True
	doc['suburb'] = suburb
	doc['sentiment'] = sentiment
	doc['topics'] = topics
	db.save(doc)
print "finished"		