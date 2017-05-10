import boto
import time
from boto.ec2.regioninfo import RegionInfo
class BotoController:
    def __init__(self,access_key_id,secret_access_key): #initialize with access_key_id and secret_access_key
        self.region=RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')
        self.ec2_conn = boto.connect_ec2(aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key,
                                         is_secure=True,region=self.region, port=8773, path='/services/Cloud',
                                         validate_certs=False)
    def createDB(self,n,key,sGroup): #create database node with number of nodes and the key used
        for i in range(int(n)):
            r = self.ec2_conn.run_instances('ami-00003b2e',key_name=key,instance_type='m2.small',
                                            security_groups=sGroup,placement = 'melbourne-np')
            instance = r.instances[0]
            index = len(self.ec2_conn.get_all_instances())
            self.addTag(instance,'Name','Database-' + str(index))
            self.addTag(instance,'Type','database')
            self.createVolume(instance,80,'melbourne-np')

    def createVolume(self,instance,storage,location): #create volume with the instance to attach, the storage and the zone of the volume
        v = self.ec2_conn.create_volume(storage,location)
        while instance.state != 'running':
            time.sleep(1)
            print 'Wait instance',instance.id,'run'
            instance.update()
        print 'Volume',v.id,'is created'
        self.ec2_conn.attach_volume(v.id,instance.id,'/dev/vdc')
        print 'Volume',v.id,'is attached to',instance.id

    def addTag(self,instance,key,name): #create tag for an instance
        status = instance.update()
        while status != 'running':
            time.sleep(1)
            status = instance.update()
        instance.add_tag(key,name)

    def createServer(self,key,sGroup): #create server node with key
        r = self.ec2_conn.run_instances('ami-00003b2e',key_name=key,instance_type='m2.large',
                                            security_groups=sGroup,placement='melbourne-np')
        self.addTag(r.instances[0],'Name','Server')
        self.addTag(r.instances[0],'Type','server')

    def createSpark(self,key,sGroup): #create server node with key
        r = self.ec2_conn.run_instances('ami-00003b2e',key_name=key,instance_type='m2.large',
                                            security_groups=sGroup,placement='melbourne')
        self.addTag(r.instances[0],'Name','Spark')
        self.addTag(r.instances[0],'Type','spark')

    def createSnapshot(self,volume_id,time): #create snapshot for volume
        self.ec2_conn.create_snapshot(volume_id,str(volume_id) + str(time))
        print 'Snapshot is created for volume ' + str(volume_id)

    def recoveryVolume(self,snapshot_id,instance_id):
        s = self.ec2_conn.get_all_snapshots([snapshot_id])
        new_vol = s.create_volume('melbourne-np')
        self.ec2_conn.attach_volume(new_vol.id,instance_id,'/dev/vdd')

    def deleteAll(self): #delete all instances, volumes and Snapshots
        v = self.ec2_conn.get_all_volumes()
        for e in v:
            if e.attachment_state() != None:
                self.ec2_conn.detach_volume(e.id)
                e.update()
            while e.attachment_state() != None:
                time.sleep(1)
                print e.attachment_state()
                e.update()
            print 'Volume',e.id, 'is detached.'
        for e in v:
            self.ec2_conn.delete_volume(e.id)
            print 'Volume',e.id,'is deleted.'
        r = self.ec2_conn.get_all_instances()
        for i in r:
            self.ec2_conn.terminate_instances(i.instances[0].id)
            print 'Instance',i.instances[0].id,'is terminated.'

    def deleteSnapshots(self, id): #delete Snapshots
        self.ec2_conn.delete_snapshot(id)
        print 'Snapshot',id,'is deleted.'

    def deleteInstance(self,id): #delte Instance
        self.ec2_conn.terminate_instances(id)
        print 'Instance',id,'is terminated.'

    def deleteVolume(self,id):
        v = self.ec2_conn.get_all_volumes([id])
        while v.attachment_state() != None:
            time.sleep(1)
            print v.attachment_state()
            v.update()
        print 'Volume',e.id, 'is detached.'
        self.ec2_conn.delete_volume(id)

    def exportInventoryFile(self): #create inventory file for ansible
        f = file('ansibleinventory.yaml','w')
        r = self.ec2_conn.get_all_instances()
        database = []
        server = []
        spark = []
        for e in r:
            instance = e.instances[0]
            typename = instance.tags['Type']
            while instance.update() != 'running':
                time.sleep(1)
            ip = instance.private_ip_address
            if typename == 'database':
                database.append(ip)
            elif typename == 'server':
                server.append(ip)
            elif typename == 'spark':
                spark.append(ip)
        f.write('[dbs]\n')
        for e in database:
            f.write('ubuntu@')
            f.write(e)
            f.write('\n')
        f.write('[server]\n')
        for e in server:
            f.write('ubuntu@')
            f.write(e)
            f.write('\n')
        f.write('[spark]\n')
        for e in spark:
            f.write('ubuntu@')
            f.write(e)
            f.write('\n')
        f.close()
