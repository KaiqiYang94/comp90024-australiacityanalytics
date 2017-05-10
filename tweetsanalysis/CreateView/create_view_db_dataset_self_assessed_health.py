 # -------------------------------
 # Team 24
 # Kaiqi Yang 729687
 # Xing Hu 733203
 # Ziyuan Wang 735953
 # Chi Che 823488
 # Yanqin Jin 787723
 # -------------------------------
# This program is used to create views for DB dataset_self_assessed_health

import couchdb

with open('./MapReduceFunctions/poor_selfassessed_health_rate.js') as f:
    poor_selfassessed_health_rate = f.read()

design_doc = {
    "_id": "_design/health_analysis",
    "language": "javascript",
    "views": {
        "poor_selfassessed_health_rate": {
            "map": poor_selfassessed_health_rate
        }
    }
}

couch = couchdb.Server('http://admin:password@127.0.0.1:5984')
db = couch['dataset_self_assessed_health']

id = "_design/health_analysis"
if id in db:
	del db[id]

db.save(design_doc)
