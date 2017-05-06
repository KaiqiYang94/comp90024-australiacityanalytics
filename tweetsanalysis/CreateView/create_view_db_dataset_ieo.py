# This program is used to create views for DB dataset_ieo

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

couch = couchdb.Server('http://admin:password@127.0.0.1:5984')
db = couch['dataset_ieo']

id = "_design/ieo_analysis"
if id in db:
	del db[id]

db.save(design_doc)
