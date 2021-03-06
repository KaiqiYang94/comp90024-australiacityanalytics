 # -------------------------------
 # Team 24
 # Kaiqi Yang 729687
 # Xing Hu 733203
 # Ziyuan Wang 735953
 # Chi Che 823488
 # Yanqin Jin 787723
 # -------------------------------

import couchdb

couch = couchdb.Server('http://admin:password@127.0.0.1:5984')
dataset_db = couch['dataset_ieo']
tweets_db = couch['tweets']

dataset_results = dataset_db.view('analysis/ieo_score')
print "dataset", len(dataset_results)
dataset_suburbs = []
for row in dataset_results:
    dataset_suburbs.append(row.key)
    # print row.value

tweet_results = tweets_db.view(
    'tweets_analysis/sentiment_analysis', reduce=True, group_level=2)

tweet_suburbs = []
for row in tweet_results:
    if row.key[0] not in tweet_suburbs:
        tweet_suburbs.append(row.key[0])
    # print row.value
    # print row.key
print "tweet", len(tweet_suburbs)


same_suburbs = set()
for ts in tweet_suburbs:
    for ds in dataset_suburbs:
        if ts in ds:
            same_suburbs.add(ts)

print "same", len(same_suburbs)

for s in tweet_suburbs:
    print s
    print ""
