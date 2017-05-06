# This program is used to create views for DB Tweets

import couchdb

with open('./MapReduceFunctions/filter_tweets_with_coordinates_inside_melbourne.js') as f:
    within_melb_map = f.read()

with open('./MapReduceFunctions/sentiment_summary_map.js') as f:
    sentiment_map = f.read()

with open('./MapReduceFunctions/tweets_reduce.js') as f:
    reduce = f.read()

with open('./MapReduceFunctions/filter_tweets_with_tump.js') as f:
    filter_tweets_with_tump = f.read()

with open('./MapReduceFunctions/tweets_with_vulgar_word.js') as f:
    tweets_with_vulgar_word = f.read()
	
with open('./MapReduceFunctions/filter_tweets_with_health.js') as f:
    filter_tweets_with_health = f.read()
	
with open('./MapReduceFunctions/monitor_processed_number.js') as f:
    monitor_processed_number = f.read()
	
with open('./MapReduceFunctions/monitor_processed_number_rereduce.js') as f:
    monitor_processed_number_rereduce = f.read()

design_doc = {
    "_id": "_design/tweets_analysis",
    "language": "javascript",
    "views": {
        "filter_tweets_with_coordinates_inside_melbourne": {
            "map": within_melb_map
        },
        "sentiment_summary": {
            "map": sentiment_map,
            "reduce": reduce
        },
        "filter_tweets_with_tump": {
            "map": filter_tweets_with_tump,
			"reduce": reduce
        },
		"filter_tweets_with_health": {
            "map": filter_tweets_with_health,
			"reduce": reduce
        },
        "tweets_with_vulgar_word": {
            "map": tweets_with_vulgar_word,
			"reduce": reduce
        },
		"monitor_processed_number": {
            "map": monitor_processed_number,
			"reduce": monitor_processed_number_rereduce
        }
    }
}

couch = couchdb.Server()
db = couch['tweets']

id = "_design/tweets_analysis"
if id in db:
	del db[id]

db.save(design_doc)
