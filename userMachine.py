import os
import pexpect

ssh_config_file = open("/etc/ssh/sshd_config", "r")
new_ssh_config_file = open("/etc/ssh/sshd_config_2", "w")

ssh_config_file = open("/etc/ssh/sshd_config", "r")
	new_ssh_config_file = open("/etc/ssh/sshd_config_2", "w")

	count = 1

	ports = [
	]

	for line in ssh_config_file:
		if count == 55:
			new_ssh_config_file.write("PasswordAuthentication yes")
		else:
			new_ssh_config_file.write(line)

		if "Port" in line:
			ports.append(line[line.index(" ") + 1:-1])
		count += 1

	ssh_config_file.close()
	new_ssh_config_file.close()

	os.system("sudo mv /etc/ssh/sshd_config_2 /etc/ssh/sshd_config")
	os.system("sudo service ssh restart")

	for port in ports:
		os.system("sudo iptables -A INPUT -p tcp --dport " + port + " -j DROP")


