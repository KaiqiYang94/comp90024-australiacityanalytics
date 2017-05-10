from BotoControllerClass import BotoController
import boto
import time
from boto.ec2.regioninfo import RegionInfo
d = {}
with open('createInstanceConfig.txt','r') as f:#read information from config file
    for line in f:
        d[line.split(':')[0]] = line.split(':')[1].strip().split(',')
f.close()
botocontroller = BotoController(d['access_key_id'][0],d['secret_access_key'][0])#initialize
botocontroller.createSnapshot(d['volume_id'],time.strtime("%d/%m/%y"))
