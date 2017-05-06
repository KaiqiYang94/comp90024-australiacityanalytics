#This program is used to create views for DB dataset_ieo

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
