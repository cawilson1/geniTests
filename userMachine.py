ssh_config_file = open("/etc/ssh/sshd_config", "r")
new_ssh_config_file = open("/etc/ssh/sshd_config_2", "w")

	count = 1
	for line in ssh_config_file:
		if count == 55:
			new_ssh_config_file.write("PasswordAuthentication yes")
		else:
			new_ssh_config_file.write(line)
		count += 1

	ssh_config_file.close()
	new_ssh_config_file.close()

	os.system("sudo mv /etc/ssh/sshd_config_2 /etc/ssh/sshd_config")
	os.system("sudo service ssh restart")


