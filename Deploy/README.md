

To run deploy the cloud:
	
	1. run the Boto script to build instance. Use
		python DeployCloud.py
	
	2. Run the install playbook to install couchdb and initialize the server
		ansible-playbook InstallCouchdb.yml  -i ansibleinventory.yaml --private-key /Users/KaiqiYang/Documents/MasterCourse/Cloud/Assignment2/cloud.key
	
	3. Run another playbook to form a cluster.
		ansible-playbook FormCluster.yml  -i ansibleinventory.yaml --private-key /Users/KaiqiYang/Documents/MasterCourse/Cloud/Assignment2/cloud.key

	4. Now ssh into one of the server, you should found the source code and when you run
		curl http://admin:password@127.0.0.1:5984/_membership
		You should see that all the node are now a cluster.