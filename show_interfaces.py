import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

cmd='show int desc'


host1='router1'
ssh.connect(host1, port=22, username='cisco', password='cisco', allow_agent=False,look_for_keys=False)
stdin,stdout,stderr = ssh.exec_command(cmd)
output_router1=stdout.readlines()
print '\n' + host1 + "                       "+ cmd +'\n'.join(output_router1)

print '\n' + "******************************************************************************************"

host2='router2'
ssh.connect(host2, port=22, username='cisco', password='cisco', allow_agent=False,look_for_keys=False)
stdin,stdout,stderr = ssh.exec_command(cmd)
output_router2=stdout.readlines()
print '\n' + host2 + "                       "+ cmd +'\n'.join(output_router2)  + '\n'
