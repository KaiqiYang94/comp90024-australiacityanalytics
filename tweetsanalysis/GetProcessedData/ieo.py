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
dataset_db = couch['dataset_ieo']

# get top 10 suburbs with highest education/ocupation score
dataset_results = dataset_db.view(
    'ieo_analysis/ieo_score', limit=10, descending=True)
for row in dataset_results:
    print row.key
    print row.value
	
print "================================================"	
# get 10 suburbs with LOWEST education/ocupation score
dataset_results = dataset_db.view(
    'ieo_analysis/ieo_score', limit=10)
for row in dataset_results:
    print row.key
    print row.value
