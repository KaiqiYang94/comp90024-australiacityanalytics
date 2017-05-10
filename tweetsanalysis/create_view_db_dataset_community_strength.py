#This program is used to create views for DB dataset_community_strength
# Name: Che Chi
# Student No.: 823488
# Email: cche2@student.unimelb.edu.au

import couchdb

with open('./MapReduceFunctions/voluntary_work_rate.js') as f:
	voluntary_work_rate = f.read()

design_doc = {
  "_id": "_design/voluntary_work_analysis",
  "language": "javascript",
  "views": {
    "voluntary_work_rate": {
      	"map": voluntary_work_rate
    }
  }
}

couch = couchdb.Server()
db = couch['dataset_community_strength']

db.save(design_doc)
