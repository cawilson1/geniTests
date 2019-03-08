#imports
import os
import pexpect

"""
#Locking down the machine for access from the KALI machine
os.system("iptables -P INPUT DROP")
os.system("iptables -P FORWARD DROP")
os.system("iptables -P OUTPUT ACCEPT")
os.system("iptables -A INPUT -s user -j ACCEPT")
"""
#directory creation
os.system("sudo mkdir /home/jDoe")
os.system("sudo mkdir /home/jDoe/Pictures")
os.system("sudo mkdir /home/jDoe/Documents")
os.system("sudo mkdir /home/jDoe/Music")
os.system("sudo mkdir /home/jDoe/Pictures/Wallpapers")

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
os.system("cd /etc/init.d")
os.system("sudo inetd restart")


#creating a vulnerable user and password
os.system("sudo useradd jDoe")
child = pexpect.spawn("sudo passwd jDoe")
child.expect("Enter new UNIX password: ")
child.sendline("xX53cUrEXx")
child.expect("Retype new UNIX password: ")
child.sendline("xX53cUrEXx")

#directory creation
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








