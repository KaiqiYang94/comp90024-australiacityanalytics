 # -------------------------------
 # Team 24
 # Kaiqi Yang 729687
 # Xing Hu 733203
 # Ziyuan Wang 735953
 # Chi Che 823488
 # Yanqin Jin 787723
 # -------------------------------
#This program is used to create views for DB dataset_ier

import couchdb

with open('./MapReduceFunctions/wealth_score.js') as f:
	wealth_score = f.read()

design_doc = {
  "_id": "_design/ier_analysis",
  "language": "javascript",
  "views": {
    "wealth_score": {
      	"map": wealth_score
    }
  }
}

couch = couchdb.Server('http://admin:password@127.0.0.1:5984')
db = couch['dataset_ier']

id = "_design/ier_analysis"
if id in db:
	del db[id]

db.save(design_doc)
