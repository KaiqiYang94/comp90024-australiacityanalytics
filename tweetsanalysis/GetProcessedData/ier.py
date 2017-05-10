import couchdb

couch = couchdb.Server()
dataset_db = couch['dataset_ier']

# get top 10 suburbs with highest wealth score
dataset_results = dataset_db.view(
    'ier_analysis/wealth_score', limit=10, descending=True)
for row in dataset_results:
    print row.key
    print row.value
