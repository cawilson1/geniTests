#imports
import os
import pexpect


#opening various ports
os.system("sudo iptables -A INPUT -p udp --dport 12345 -j ACCEPT")
os.system("sudo iptables -A INPUT -P udp --dport 6512 -j ACCEPT")
os.system("sudo iptables -A INPUT -p tcp --dport 578 -j ACCEPT")
os.system("sudo iptables -A INPUT -p tcp --dport 2957 -j ACCEPT")
#open telnet port and prepare it for telneting
os.system("sudo iptables -A INPUT -p tcp --dport 23 -j ACCEPT")
os.system("sudo apt-get install telnetd")
os.system("cd /etc/init.d")
os.system("sudo inetd restart")
#standard ssh port
os.system("sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT")

#creating a vulnerable user and password
os.system("sudo useradd jDoe")
child = pexpect.spawn("sudo passwd jDoe")
child.expect("Enter new UNIX password: ")
child.sendline("xX53cUrEXx")
child.expect("Retype new UNIX password: ")
child.sendline("xX53cUrEXx")

#creating a hidden file with the stegnographic in it
os.system("echo \"The passphrase is CanadaIsGreat\" | cat > .pass.txt")
os.system("wget https://raw.githubusercontent.com/Setzlerte/geniTests/master/coolSpace.jpg")


#Locking down the machine for access from the KALI machine
os.system("iptables -A INPUT -j REJECT")
os.system("iptables -A OUTPUT -j ACCEPT")
os.system("iptables -A OUTPUT -o lo -j ACCEPT")


