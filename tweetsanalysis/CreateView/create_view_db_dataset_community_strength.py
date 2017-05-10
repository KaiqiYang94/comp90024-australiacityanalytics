# This program is used to create views for DB dataset_community_strength

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

couch = couchdb.Server('http://admin:password@127.0.0.1:5984')
db = couch['dataset_community_strength']

id = "_design/voluntary_work_analysis"
if id in db:
	del db[id]

db.save(design_doc)
