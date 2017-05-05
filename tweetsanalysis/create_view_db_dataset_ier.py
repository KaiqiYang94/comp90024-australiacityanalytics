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

couch = couchdb.Server()
db = couch['dataset_ier']

db.save(design_doc)
