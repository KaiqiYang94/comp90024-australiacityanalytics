 # -------------------------------
 # Team 24
 # Kaiqi Yang 729687
 # Xing Hu 733203
 # Ziyuan Wang 735953
 # Chi Che 823488
 # Yanqin Jin 787723
 # -------------------------------
#This program is used to create views for DB dataset_life_satisfaction
# Name: Che Chi
# Student No.: 823488
# Email: cche2@student.unimelb.edu.au

import couchdb

with open('./MapReduceFunctions/avg_satisfacation.js') as f:
	avg_satisfacation = f.read()

with open('./MapReduceFunctions/high_satisfacation_percentage.js') as f:
	high_satisfacation_percentage = f.read()

with open('./MapReduceFunctions/low_satisfacation_percentage.js') as f:
	low_satisfacation_percentage = f.read()

design_doc = {
  "_id": "_design/life_satisfacation_summary",
  "language": "javascript",
  "views": {
    "avg_satisfacation": {
      	"map": avg_satisfacation
    },
    "high_satisfacation_percentage": {
    	"map": high_satisfacation_percentage
    },
    "low_satisfacation_percentage": {
    	"map": low_satisfacation_percentage
    }
  }
}

couch = couchdb.Server()
db = couch['dataset_life_satisfaction']

db.save(design_doc)
