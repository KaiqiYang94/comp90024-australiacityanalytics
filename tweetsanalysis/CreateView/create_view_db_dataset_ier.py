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

db.save(design_doc)
