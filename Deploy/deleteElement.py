from BotoControllerClass import BotoController
import boto
from boto.ec2.regioninfo import RegionInfo
d = {}
with open('deployConfig.txt','r') as f:#read information from config file
    for line in f:
        d[line.split(':')[0]] = line.split(':')[1].strip().split(',')
f.close()
botocontroller = BotoController(d['access_key_id'][0],d['secret_access_key'][0])#initialize
if d['type'] == 'instance':
    botocontroller.deleteInstance(d['id'])
elif d['type'] == 'volume':
    botocontroller.deleteVolume(d['id'])
elif d['type'] == 'snapshots':
    botocontroller.deleteSnapshots(d['id'])
else:
    print 'Wrong type'
botocontroller.exportInventoryFile()#create ansible inventory file
