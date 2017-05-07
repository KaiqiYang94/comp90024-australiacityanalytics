import couchdb

couch = couchdb.Server()
dataset_db = couch['dataset_life_satisfaction']

# get top 10 suburbs with high average life satisfacation
dataset_results = dataset_db.view(
    'life_satisfacation_summary/avg_satisfacation', limit=10, descending=True)
for row in dataset_results:
    print row.key
    print row.value
