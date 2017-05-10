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
dataset_db = couch['dataset_community_strength']

# get top 10 suburbs with highest voluntary work rate
dataset_results = dataset_db.view(
    'voluntary_work_analysis/voluntary_work_rate', limit=10, descending=True)
for row in dataset_results:
    print row.key
    print row.value
