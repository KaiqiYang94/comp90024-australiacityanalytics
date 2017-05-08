import couchdb
from collections import defaultdict

couch = couchdb.Server('http://admin:password@127.0.0.1:5984')
tweets_db = couch['tweets']
try:
    summary_db = couch['tweets_summary']
except:
    summary_db = couch.create('tweets_summary')

###sentiment
sentiments = tweets_db.view('tweets_analysis/sentiment_summary', reduce = True, group_level = 2)

suburb_sentiments = defaultdict(dict)
for row in sentiments:
	suburb_sentiments[row.key[0]][row.key[1]] = row.value

###vulgar words
vulgars = tweets_db.view('tweets_analysis/tweets_with_vulgar_word',reduce = True, group_level = 2)
suburb_vulgar = {}
for row in vulgars:
	suburb_vulgar[row.key] = row.value;

###trump
trump = tweets_db.view('tweets_analysis/filter_tweets_with_tump',reduce = True, group_level = 2)
suburb_trump = defaultdict(dict)
for row in trump:
	suburb_trump[row.key[0]][row.key[1]] = row.value
	
###health
health = tweets_db.view('tweets_analysis/filter_tweets_with_health',reduce = True, group_level = 2)
suburb_health = defaultdict(dict)
for row in trump:
	suburb_health[row.key[0]][row.key[1]] = row.value

###save summary
suburbs = suburb_sentiments.keys()
for suburb in suburbs:
	id = suburb
	
	sentiments = suburb_sentiments.get(id)
	tweet_number = sum(sentiments.values())
	if tweet_number > 2:
		positive_tweets_no = sentiments.get("positive", 0)
		negative_tweets_no = sentiments.get("negative", 0)
		positive_rate = float(positive_tweets_no) / tweet_number
		negative_rate = float(negative_tweets_no) / tweet_number	
		
		trumps = suburb_trump.get(id)
		if trumps == None:
			trump_positive_rate = 0
			trump_negative_rate = 0
		else:
			trump_no = sum(trumps.values())
			trump_positive_no = trumps.get("positive", 0)
			trump_negative_no = trumps.get("negative", 0)
			trump_positive_rate = float(trump_positive_no) / trump_no
			trump_negative_rate = float(trump_negative_no) / trump_no
			
		healths = suburb_health.get(id)
		if healths == None:
			health_positive_rate = 0
			health_negative_rate = 0
		else:
			health_no = sum(healths.values())
			health_positive_no = healths.get("positive", 0)
			health_negative_no = healths.get("negative", 0)
			health_positive_rate = float(health_positive_no) / health_no
			health_negative_rate = float(health_negative_no) / health_no
		
		vulgar_no = suburb_vulgar.get(id, 0)
		vulgar_rate = float(vulgar_no) / tweet_number
		
		if id in summary_db:
			doc = summary_db.get(id)
			doc['positive_rate'] = positive_rate
			doc['negative_rate'] = negative_rate
			doc['trump_positive_rate'] = trump_positive_rate
			doc['trump_negative_rate'] = trump_negative_rate
			doc['health_positive_rate'] = health_positive_rate
			doc['health_negative_rate'] = health_negative_rate
			doc['vulgar_rate'] = vulgar_rate
		else:
			doc = {'_id': id, 'suburb': id, 'positive_rate': positive_rate, 'negative_rate': negative_rate,
					'trump_positive_rate': trump_positive_rate, 'trump_negative_rate': trump_negative_rate,
					'health_positive_rate': health_positive_rate, 'health_negative_rate': health_negative_rate,
					'vulgar_rate': vulgar_rate}
					
		summary_db.save(doc)

