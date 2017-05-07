import couchdb

couch = couchdb.Server()
dataset_db = couch['dataset_community_strength']

# get top 10 suburbs with highest voluntary work rate
dataset_results = dataset_db.view(
    'voluntary_work_analysis/voluntary_work_rate', limit=10, descending=True)
for row in dataset_results:
    print row.key
    print row.value
