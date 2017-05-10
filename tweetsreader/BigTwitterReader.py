import paramiko
from couchdb import Server
import json

server = Server('http://admin:password@127.0.0.1:5984/')
try:
    db_tweets = server['tweets']
except:
    db_tweets = server.create('tweets')

username = "ziyuanw"
password = "19910816"

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
ssh.connect('spartan2.hpc.unimelb.edu.au', username=username,
            password=password)

print('----------------Start reading--------------------------')


sftp = ssh.open_sftp()
doc = sftp.open('bigTwitter.json', 'r')
temp = doc.readline()

line = doc.readline()

while line.strip() != "]":

    data = json.loads(line.replace('}}},', '}}}'))

    nid = data['json']['id_str']

    if nid in db_tweets:
        print('--------already have----------------')
    else:
        ntext = data['json']['text']
        ncoordinates = data['json']['coordinates']['coordinates']
        nuser = data['json']['user']
        ntime = data['json']['created_at']
        nplace = data['json']['place']
        nentities = data['json']['entities']
        ndoc = {'_id': nid, 'text': ntext, 'user': nuser,
                'coordinates': ncoordinates, 'create_time': ntime,
                'place': nplace, 'entities': nentities,
                'addressed': False}
        db_tweets.save(ndoc)
        print(nid)
        print('-------------------------------------')
    line = doc.readline()

print('--------------finish read bigTwitter-------------------------')
doc.close
sftp.close
ssh.close
