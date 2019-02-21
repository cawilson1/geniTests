#imports
import os
import pexpect


#opening various ports
os.system("sudo iptables -A INPUT -p udp --dport 12345 -j ACCEPT")
os.system("sudo iptables -A INPUT -P udp --dport 6512 -j ACCEPT")
os.system("sudo iptables -A INPUT -p tcp --dport 578 -j ACCEPT")
os.system("sudo iptables -A INPUT -p tcp --dport 2957 -j ACCEPT")
#standard telnet port
os.system("sudo iptables -A INPUT -p tcp --dport 23 -j ACCEPT")
#standard ssh port
os.system("sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT")

#creating a vulnerable user and password
os.system("sudo useradd jDoe")
child = pexpect.spawn("sudo passwd jDoe")
child.expect("Enter new UNIX password: ")
child.sendline("password")
child.expect("Retype new UNIX password: ")
child.sendline("password")

#creating a hidden file with the open ports in it
os.system("echo \"Open Ports: \n12345 \n6512 \n578 \n2957 \n23 \n22\" | cat > .openPorts.txt")



