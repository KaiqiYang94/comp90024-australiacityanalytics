{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf820
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import boto\
import time\
from boto.ec2.regioninfo import RegionInfo\
class BotoController:\
    def __init__(self,access_key_id,secret_access_key):\
        self.region=RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au') \
        self.ec2_conn = boto.connect_ec2(aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key, is_secure=True,region=self.region, port=8773, path='/services/Cloud', validate_certs=False)\
        self.dbip = []\
        serverip = None\
    def createDB(self,n):\
        for i in range(n):\
            r = self.ec2_conn.run_instances('ami-00003b2e',key_name='test_key',instance_type='m2.small',\
                                            security_groups=['default'],placement = 'melbourne')\
            instance = r.instances[0]\
            v = self.ec2_conn.create_volume('80','melbourne-np')\
\
            while instance.state == 'pending':\
                time.sleep(1)\
                instance.update()\
            self.ec2_conn.attach_volume(v.id,r.instances[0].id,'/dev/vdc')\
            self.dbip.append(r.instances[0].ip_address)\
    def createServer(self):\
            r = self.ec2_conn.run_instances('ami-00003b2e',key_name='test_key',instance_type='m2.large',\
                                            security_groups=['default'],placement='melbourne')\
            self.serverip = r.instances[0].ip_address}