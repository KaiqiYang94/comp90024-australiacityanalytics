# -------------------------------
# Team 24
# Kaiqi Yang 729687
# Xing Hu 733203
# Ziyuan Wang 735953
# Chi Che 823488
# Yanqin Jin 787723
# -------------------------------



from BotoControllerClass import BotoController
import boto
from boto.ec2.regioninfo import RegionInfo
d = {}
with open('createInstanceConfig.txt','r') as f:#read information from config file
    for line in f:
        d[line.split(':')[0]] = line.split(':')[1].strip().split(',')
f.close()
botocontroller = BotoController(d['access_key_id'][0],d['secret_access_key'][0])#initialize
if d['type'] == 'database':
    botocontroller.createDB(d['number'][0],d['key'][0],d['securityGroups'])#create db
elif d['type'] == 'server':
    for i in range(d['number']):
        botocontroller.createServer(d['key'],d['securityGroups'])#create server
elif d['type'] == 'spark':
    for i in range(d['number']):
        botocontroller.createSpark(d['key'],d['securityGroups'])#create server
else:
    print 'Wrong type!'
botocontroller.exportInventoryFile()#create ansible inventory file
