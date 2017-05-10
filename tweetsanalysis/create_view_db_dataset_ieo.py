 # -------------------------------
 # Team 24
 # Kaiqi Yang 729687
 # Xing Hu 733203
 # Ziyuan Wang 735953
 # Chi Che 823488
 # Yanqin Jin 787723
 # -------------------------------
#This program is used to create views for DB dataset_ieo
# Name: Che Chi
# Student No.: 823488
# Email: cche2@student.unimelb.edu.au

import couchdb

with open('./MapReduceFunctions/ieo_score.js') as f:
	ieo_score = f.read()

design_doc = {
  "_id": "_design/ieo_analysis",
  "language": "javascript",
  "views": {
    "ieo_score": {
      	"map": ieo_score
    }
  }
}

couch = couchdb.Server()
db = couch['dataset_ieo']

db.save(design_doc)
