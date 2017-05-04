import paramiko

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
ssh.connect('spartan2.hpc.unimelb.edu.au', username='xingh1',
            password='911027.com')

print('----------------Start reading--------------------------')

# stdin, stdout, stderr = ssh.exec_command('cat tinyTwitter.json')
# net_dump = stdout.readline()
# print(net_dump)
sftp = ssh.open_sftp()
doc = sftp.open('tinyTwitter.json', 'r')
line = doc.readline()
print(line)
line = doc.readline()
print(line)
doc.close
sftp.close
ssh.close
