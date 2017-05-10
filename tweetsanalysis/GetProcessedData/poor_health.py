 # -------------------------------
 # Team 24
 # Kaiqi Yang 729687
 # Xing Hu 733203
 # Ziyuan Wang 735953
 # Chi Che 823488
 # Yanqin Jin 787723
 # -------------------------------
import couchdb

couch = couchdb.Server()
dataset_db = couch['dataset_self_assessed_health']

# get top 10 suburbs with highest poor self assessed health rate
dataset_results = dataset_db.view(
    'health_analysis/poor_selfassessed_health_rate', limit=10, descending=True)
for row in dataset_results:
    print row.key
    print row.value
