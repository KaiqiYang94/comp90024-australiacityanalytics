import couchdb

couch = couchdb.Server()
dataset_db = couch['dataset_life_satisfaction']

#get top 10 suburbs with high average life satisfacation
avg_results = dataset_db.view('life_satisfacation_summary/avg_satisfacation', limit = 10, descending = True)
for row in avg_results:
	print row.key
	print row.value

print "========================================================"
#get top 10 suburbs with percentage of high satisfacation	
high_results = dataset_db.view('life_satisfacation_summary/high_satisfacation_percentage', limit = 10, descending = True)
for row in high_results:
	print row.key
	print row.value

print "========================================================"
#get top 10 suburbs with percentage of low satisfacation	
low_results = dataset_db.view('life_satisfacation_summary/low_satisfacation_percentage', limit = 10, descending = True)
for row in low_results:
	print row.key
	print row.value
	
