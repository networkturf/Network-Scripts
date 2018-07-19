import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
routers = ['switch_prod','switch_dmz','router_internet']

for i in routers:
   ssh.connect(i, port=22, username='srv', password='password', allow_agent=False,look_for_keys=False)
   stdin,stdout,stderr = ssh.exec_command('copy startup-config tftp://10.202.213.77/%s'%(i))

