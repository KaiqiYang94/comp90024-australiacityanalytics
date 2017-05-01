#This is the whole process of deploy a couchdb cluster to the Nectar
# is using the shell script
# will be transfered to Ansible to make it run automatically


#https://www.zybuluo.com/contribute/note/663385
#https://github.com/afiskon/install-couchdb/blob/master/install-couchdb.sh


set -e

sudo apt-get update || true
sudo apt-get --no-install-recommends -y install \
    build-essential pkg-config runit erlang \
    libicu-dev libmozjs185-dev libcurl4-openssl-dev

wget http://apache-mirror.rbc.ru/pub/apache/couchdb/source/2.0.0/apache-couchdb-2.0.0.tar.gz

tar -xvzf apache-couchdb-2.0.0.tar.gz
cd apache-couchdb-2.0.0/
./configure && make release

	# to edit the file 
		# #!/bin/bash

		# addr=$1
		# port=$2
		# user=$3

		# sed -i -e "s/\(address=\).*/\1$1/" \
		# -e "s/\(port=\).*/\1$2/" \
		# -e "s/\(username=\).*/\1$3/" xyz.cfg

		#! /bin/sh
		# file=xyz.cfg
		# addr=$1
		# port=$2
		# username=$3
		# sed -i 's/address=.*/address='$addr'/' $file
		# sed -i 's/port=.*/port='$port'/' $file
		# sed -i 's/username=.*/username='$username'/' $file

	# Execute the shell script
	# $ ./script.sh 127.8.7.7 7822 xyz_ITR4

	# $ cat xyz.cfg
	# group address=127.8.7.7
	# port=7822
	# Jboss username=xyz_ITR4


# 集群配置

# 	注意：所有的集群节点设置为相同的用户名和密码。 
# 	修改配置：COUCHDB_HOME/rel/couchdb/etc/local.ini 为：

# 		[chttpd]
# 		bind_address = 0.0.0.0
# 		[admins]
# 		admin = password　# 用户名和密码
	
# 	修改配置：COUCHDB_HOME/rel/couchdb/etc/vm.agrs，假设本节点的ip为192.168.199.236，则修改为：

# 		-name couchdb@192.168.199.236

# 	修改配置：COUCHDB_HOME/rel/couchdb/releases/2.0.0/sys.config为：

# [
#     {lager, [
#         {error_logger_hwm, 1000},
#         {error_logger_redirect, true},
#         {handlers, [
#             {lager_console_backend, [debug, {
#                 lager_default_formatter,
#                 [
#                     date, " ", time,
#                     " [", severity, "] ",
#                     node, " ", pid, " ",
#                     message,
#                     "\n"
#                 ]
#             }]}
#         ]},
#         {inet_dist_listen_min, 9100},
#         {inet_dist_listen_max, 9200}
#     ]}
# ].

sudo adduser --system \
        --no-create-home \
        --shell /bin/bash \
        --group --gecos \
        "CouchDB Administrator" couchdb

sudo cp -R rel/couchdb /home/couchdb
sudo chown -R couchdb:couchdb /home/couchdb
sudo find /home/couchdb -type d -exec chmod 0770 {} \;
sudo sh -c 'chmod 0644 /home/couchdb/etc/*'

sudo mkdir /var/log/couchdb
sudo chown couchdb:couchdb /var/log/couchdb

sudo mkdir /etc/sv/couchdb
sudo mkdir /etc/sv/couchdb/log

cat > run << EOF
#!/bin/sh
export HOME=/home/couchdb
exec 2>&1
exec chpst -u couchdb /home/couchdb/bin/couchdb
EOF

cat > log_run << EOF
#!/bin/sh
exec svlogd -tt /var/log/couchdb
EOF

sudo mv ./run /etc/sv/couchdb/run
sudo mv ./log_run /etc/sv/couchdb/log/run

sudo chmod u+x /etc/sv/couchdb/run
sudo chmod u+x /etc/sv/couchdb/log/run

sudo ln -s /etc/sv/couchdb/ /etc/service/couchdb

sleep 5
sudo sv status couchdb


# 集群节点添加

#如果需要建立cluster

	# 如果添加192.168.199.189,在192.168.199.189上按照上述步骤走一遍，将ip更换为192.168.199.189即可。

	# 在192.168.199.236节点上添加192.168.199.189节点：

	# curl -X POST -H "Content-Type: application/json" http://admin:password@127.0.0.1:5984/_cluster_setup -d '{"action": "enable_cluster", "bind_address":"0.0.0.0", "username": "admin", "password":"password", "port": 5984, "remote_node": "192.168.199.189", "remote_current_user": "admin", "remote_current_password": "password" }'
	# curl -X POST -H "Content-Type: application/json" http://admin:password@127.0.0.1:5984/_cluster_setup -d '{"action": "add_node", "host":"192.168.199.189", "port": "5984", "username": "admin", "password":"password"}'
	# curl -X POST -H "Content-Type: application/json" http://admin:password@127.0.0.1:5984/_cluster_setup -d '{"action": "finish_cluster"}'


# # 如果建好cluster之后再加节点
	# curl -X POST -H "Content-Type: application/json" http://admin:password@127.0.0.1:5984/_cluster_setup -d '{"action": "enable_cluster", "bind_address":"0.0.0.0", "username": "admin", "password":"password", "port": 5984, "remote_node": "115.146.92.175", "remote_current_user": "admin", "remote_current_password": "password" }'
	# curl -X PUT "http://admin:password@127.0.0.1:5986/_nodes/couchdb@115.146.92.175" -d {}

# curl http://admin:password@127.0.0.1:5984/_membership

	
# 访问http://127.0.0.1:5984/_membership时能看到如下返回的数据：

# {
#     all_nodes: [
#         "couchdb@192.168.199.189",
#         "couchdb@192.168.199.236"
#     ],
#     cluster_nodes: [
#         "couchdb@192.168.199.189",
#         "couchdb@192.168.199.236"
#     ]
# }

# curl http://admin:password@127.0.0.1:5984/_all_dbs
# 这表示集群搭建成功。或如果在192.168.199.236上的couchdb中添加一个数据库表，如果能在192.168.199.189上的couchdb中看到，表示安装成功。


# curl -X PUT http://127.0.0.1:5984/my_database/"001" -d '{ " Name " : " Raju " , " age " :" 23 " , " Designation " : " Designer " }'

# curl -X PUT http://admin:password@127.0.0.1:5984/the_test_db/"001" -d '{ " Name " : " Raju " , " age " :" 23 " , " Designation " : " Designer " }'

# curl -X GET http://admin:password@127.0.0.1:5984/the_test_db/001



# Copy local files to the cloud 
# scp -r /Users/KaiqiYang/Documents/Learning/JavaProj/BitBucketPrivateRepo/CloudTestProject/Example/  kaiqi@130.56.253.113:/home/kaiqi/uploadfiles

# To get some id or changes 
# curl -X GET http://admin:password@127.0.0.1:5984/tweets/_changes?descending=true&limit=1


# install pip

# make file system

# back up couch db

# deploy website 

# assign accounts
