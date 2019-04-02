#imports
import os
import pexpect

"""
#Locking down the machine for access from the KALI machine
##os.system("iptables -P INPUT DROP")
os.system("iptables -P FORWARD DROP")
os.system("iptables -P OUTPUT ACCEPT")
os.system("iptables -A INPUT -s 10.10.1.1 -j ACCEPT")
os.system("iptables -A INPUT -s 10.10.1.2 -j ACCEPT")
#opening input from port 3000 so that the OWASP juiceshop can run
os.system("iptables -A INPUT -p tcp --dport 3000 -j ACCEPT")
os.system("iptables -A INPUT -p udp --dport 3000 -j ACCEPT")
"""
#opening various ports
os.system("sudo iptables -A INPUT -p udp --dport 12345 -j ACCEPT")
os.system("sudo iptables -A INPUT -P udp --dport 6512 -j ACCEPT")
os.system("sudo iptables -A INPUT -p tcp --dport 578 -j ACCEPT")
os.system("sudo iptables -A INPUT -p tcp --dport 2957 -j ACCEPT")
#standard ssh port
os.system("sudo iptables -A INPUT --dport 22 -j ACCEPT")
#open telnet port and prepare it for telneting
os.system("sudo iptables -A INPUT -p tcp --dport 23 -j ACCEPT")
os.system("sudo apt-get install telnetd")
os.system("cd /etc/init.d && sudo inetd restart")


#creating a vulnerable user and password
os.system("sudo useradd jDoe")
child = pexpect.spawn("sudo passwd jDoe")
child.expect("Enter new UNIX password: ")
child.sendline("xX53cUrEXx")
child.expect("Retype new UNIX password: ")
child.sendline("xX53cUrEXx")

#juice-shop setup and run
os.system("curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -")
os.system("sudo apt-get install -y nodejs")
os.system("wget https://github.com/bkimminich/juice-shop/releases/download/v8.4.1/juice-shop-8.4.1_node10_linux_x64.tgz")
os.system("tar -xzvf juice-shop-8.4.1_node10_linux_x64.tgz")
os.system("cd juice-shop_8.4.1 && sudo npm start &")



#directory creation for authenticity
os.system("sudo mkdir /home/jDoe")
os.system("sudo mkdir /home/jDoe/Pictures")
os.system("sudo mkdir /home/jDoe/Documents")
os.system("sudo mkdir /home/jDoe/Music")
os.system("sudo mkdir /home/jDoe/Pictures/Wallpapers")

#populating directories
os.system("cd /home/jDoe")
os.system("cd /home/jDoe/Documents")
#creating a hidden file with the stegnographic passphrase in it
os.system("echo \"The passphrase is CanadaIsGreat\" | cat > .pass.txt")
os.system("sudo wget -P /home/jDoe/Documents https://raw.githubusercontent.com/Setzlerte/geniTests/master/bulkFiles/History%20of%20Canada.txt")
os.system("sudo wget -P /home/jDoe/Documents https://raw.githubusercontent.com/Setzlerte/geniTests/master/bulkFiles/aurora.txt")
os.system("sudo wget -P /home/jDoe/Documents https://raw.githubusercontent.com/Setzlerte/geniTests/master/bulkFiles/moose.txt")
os.system("sudo wget -P /home/jDoe/Pictures https://raw.githubusercontent.com/Setzlerte/geniTests/master/bulkFiles/sittingMoose.jpeg")
os.system("sudo wget -P /home/jDoe/Pictures https://raw.githubusercontent.com/Setzlerte/geniTests/master/bulkFiles/moutainsFlag.jpeg")

os.system("sudo wget -P /home/jDoe/Pictures/Wallpapers https://raw.githubusercontent.com/Setzlerte/geniTests/master/bulkFiles/underwaterNun.jpg")
os.system("sudo wget -P /home/jDoe/Pictures/Wallpapers https://raw.githubusercontent.com/Setzlerte/geniTests/master/bulkFiles/coolSpace.jpg")
os.system("sudo wget -P /home/jDoe/Pictures/Wallpapers https://raw.githubusercontent.com/Setzlerte/geniTests/master/bulkFiles/mountains.jpeg")
os.system("sudo wget -P /home/jDoe/Pictures/Wallpapers https://raw.githubusercontent.com/Setzlerte/geniTests/master/bulkFiles/mooseLights.jpeg")
os.system("sudo wget -P /home/jDoe/Pictures/Wallpapers https://raw.githubusercontent.com/Setzlerte/geniTests/master/bulkFiles/spaceJar.jpeg")

#preparing the file for SSH

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


