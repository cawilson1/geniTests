os.system("sudo useradd alice")
child = pexpect.spawn("sudo passwd alice")
child.expect("Enter new UNIX password: ")
child.sendline("password")
child.expect("Retype new UNIX password: ")
child.sendline("password")
os.system("sudo chown -R alice /home/alice")
os.system("sudo chgrp -R alice /home/alice")


ssh_config_file = open("/etc/ssh/sshd_config", "r")
new_ssh_config_file = open("/etc/ssh/sshd_config_2", "w")

count = 1

ports = []

for line in ssh_config_file:
	if count == 54:
		new_ssh_config_file.write("PasswordAuthentication yes")
	elif count == 33: 
		new_ssh_config_file.write("RSAAuthentication no")
	elif count == 34:
		new_ssh_config_file.write("PubkeyAuthentication no")
	else:
		new_ssh_config_file.write(line)
	count += 1

ssh_config_file.close()
new_ssh_config_file.close()

os.system("sudo mv /etc/ssh/sshd_config_2 /etc/ssh/sshd_config")
os.system("sudo service ssh restart")





