import couchdb

couch = couchdb.Server()
dataset_db = couch['tweets_summary']

# get top 10 suburbs with highest negative rate of trump
dataset_results = dataset_db.view(
    'tweets_summary/trump_negative_rate', limit=10, descending=True)
for row in dataset_results:
    print row.key
    print row.value