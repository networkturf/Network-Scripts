import paramiko     # this python module lets us connect to devices over ssh
ssh = paramiko.SSHClient()   # Create a variable and call the module. Variable 'ssh' is now an object, which is an instance of paramiko.SSHClient  
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # we want to accept the RSA key of the devices we want to connect to from this host. Unknown keys get added to the 'known hosts' file for that session
cmd=raw_input("Enter a command: ")   # variable 'cmd' gets assigned the command which is entered after running the program
routers=['router1','router2','core_router1','border_router2']  # variable 'routers' is a list of devices from which you want to get the show output. Replace this list with the hostnames of your network devices, provided you have a DNS mapping available; otherwise enter IP addresses
for i in routers:   # i is the iterator which iterates over the above list one by one
	ssh.connect(i, port=22, username='admin', password='password', allow_agent=False,look_for_keys=False)  # this establishes connectivity with the devices. Replace the usename and password with the appropriate values 
	stdin,stdout,stderr = ssh.exec_command(cmd)  # stdin,stdout,stderr are standard streams used to input data, output data and write error messages respectively.  
	x=stdout.readlines()   # we store the output from the devices to variable 'x'
	print '**********************************************************'	# just adds a line between outputs of various devices
	print '\n'
	print i + '          ' + cmd    # prints the name of the device and the name of the command 
	for j in x:     # iterates over the outputs from the devices in the above list
		print j   # prints those outputs 


