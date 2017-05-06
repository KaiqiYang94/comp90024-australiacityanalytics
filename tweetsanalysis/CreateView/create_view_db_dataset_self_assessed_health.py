#This program is used to create views for DB dataset_self_assessed_health

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

couch = couchdb.Server()
db = couch['dataset_self_assessed_health']

db.save(design_doc)
