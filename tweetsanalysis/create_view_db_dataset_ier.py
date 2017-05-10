 # -------------------------------
 # Team 24
 # Kaiqi Yang 729687
 # Xing Hu 733203
 # Ziyuan Wang 735953
 # Chi Che 823488
 # Yanqin Jin 787723
 # -------------------------------
#This program is used to create views for DB dataset_ier
# Name: Che Chi
# Student No.: 823488
# Email: cche2@student.unimelb.edu.au

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

couch = couchdb.Server()
db = couch['dataset_ier']

db.save(design_doc)
