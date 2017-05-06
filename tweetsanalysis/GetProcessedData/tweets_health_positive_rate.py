import couchdb

couch = couchdb.Server()
dataset_db = couch['tweets_summary']

# get top 10 suburbs with highest positive rate of health
dataset_results = dataset_db.view(
    'tweets_summary/health_positive_rate', limit=10, descending=True)
for row in dataset_results:
    print row.key
    print row.value