import couchdb

couch = couchdb.Server()
db = couch['tweets']

design_doc = {
#_id is the design document id
  "_id": "_design/inside",
  "language": "javascript",
  "views": {
#the name below is the index of the view
    "inside": {
      #"map": "function (doc) {if(!doc.addressed){lon = doc.place.bounding_box.coordinates[0][0][0];lat = doc.place.bounding_box.coordinates[0][0][1];if(insideMelbourne(lat,lon)){emit(doc._id, doc);}}}function insideMelbourne(lat, lon){if(lon>=144.5937418 && lon<=145.5125288,-38.4338593&&lat>=-38.4338593 && lat<=-37.5112737){return true;}else{return false;}}"
      "map": "function (doc){emit(doc._id, doc.text);}"
    }
  }
}
if db['_design/inside'] is not None:
	del db['_design/inside']

doc_id, doc_rev = db.save(design_doc)
print doc_id, doc_rev

results = db.view('inside/inside')
print len(results)
for row in results:
	pass
