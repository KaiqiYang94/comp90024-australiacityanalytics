import boto
from boto.ec2.regioninfo import RegionInfo
# Get region info objectß
region=RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')
# Set up connection
ec2_conn = boto.connect_ec2(aws_access_key_id="4e2749f8cd6347ca8ec42409859d8f77", aws_secret_access_key="bd6dcaf6ccfa45ac847522bd06129ee7", is_secure=True, region=region, port=8773, path='/services/Cloud', validate_certs=False)
# This is to build an instance 
#ec2_conn.run_instances('ami-00003b2e', key_name='test_key', instance_type='m2.small', security_groups=['ssh','default'])


# Get reservations:
reservations = ec2_conn.get_all_reservations()


for res in reservations:
    for inst in res.instances:
        if 'Name' in inst.tags:
            print "%s (%s) [%s]" % (inst.tags['Name'], inst.id, inst.state)
        else:
            print "%s [%s]" % (inst.id, inst.state)


# Show reservation details:
for idx, res in enumerate(reservations): 
    print idx, res.id, res.instances
# Show instance details:
print reservations[0].instances[0].ip_address 
print reservations[0].instances[0].placement


# copy the commands to the terminal and execute that 

# This is to build an instance 
#ec2_conn.run_instances('ami-00003b2e', key_name='test_key', instance_type='m2.small', security_groups=['ssh','default'])

# what if i delete some thing
