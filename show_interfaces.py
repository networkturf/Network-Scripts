import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

cmd='show int desc'


host1='rt11bo01'
ssh.connect(host1, port=22, username='kvaidya', password='shocKwave)3', allow_agent=False,look_for_keys=False)
stdin,stdout,stderr = ssh.exec_command(cmd)
output_rt11bo01=stdout.readlines()
print '\n' + host1 + "                       "+ cmd +'\n'.join(output_rt11bo01)

print '\n' + "******************************************************************************************"

host2='rt11bo02'
ssh.connect(host2, port=22, username='kvaidya', password='shocKwave)3', allow_agent=False,look_for_keys=False)
stdin,stdout,stderr = ssh.exec_command(cmd)
output_rt11bo02=stdout.readlines()
print '\n' + host2 + "                       "+ cmd +'\n'.join(output_rt11bo02)  + '\n'
