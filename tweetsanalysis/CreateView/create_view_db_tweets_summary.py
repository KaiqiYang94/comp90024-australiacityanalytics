 # -------------------------------
 # Team 24
 # Kaiqi Yang 729687
 # Xing Hu 733203
 # Ziyuan Wang 735953
 # Chi Che 823488
 # Yanqin Jin 787723
 # -------------------------------
import couchdb

with open('./MapReduceFunctions/positive_rate.js') as f:
    positive_rate = f.read()
	
with open('./MapReduceFunctions/negative_rate.js') as f:
    negative_rate = f.read()
	
with open('./MapReduceFunctions/health_positive_rate.js') as f:
    health_positive_rate = f.read()
	
with open('./MapReduceFunctions/health_negative_rate.js') as f:
    health_negative_rate = f.read()
	
with open('./MapReduceFunctions/trump_positive_rate.js') as f:
    trump_positive_rate = f.read()
	
with open('./MapReduceFunctions/trump_negative_rate.js') as f:
    trump_negative_rate = f.read()
	
with open('./MapReduceFunctions/vulgar_rate.js') as f:
    vulgar_rate = f.read()
	
design_doc = {
    "_id": "_design/tweets_summary",
    "language": "javascript",
    "views": {
        "positive_rate": {
            "map": positive_rate
        },
        "negative_rate": {
            "map": negative_rate
        },
        "health_positive_rate": {
            "map": health_positive_rate
        },
		"health_negative_rate": {
            "map": health_negative_rate
        },
        "trump_positive_rate": {
            "map": trump_positive_rate
        },
		"trump_negative_rate": {
            "map": trump_negative_rate
        },
		"vulgar_rate": {
            "map": vulgar_rate
        }
    }
}

couch = couchdb.Server('http://admin:password@127.0.0.1:5984')
try:
    db = couch['tweets_summary']
except:
    db = couch.create('tweets_summary')

id = "_design/tweets_summary"
if id in db:
	del db[id]

db.save(design_doc)