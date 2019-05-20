# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:54:20 2019

@author: Casey Wilson

python menu to create rspec
"""

import os
import sys
import python2_rspec_menu
from RspecMenuItem import RspecMenuItem

#returns given arg, and returns default boolean if no match is found
def getBool(arg,default):
    if arg == 'n' or arg == 'no' or arg == 'N' or arg == 'No' or arg == 'NO':
        return False
    if arg == 'y' or arg == 'yes' or arg == 'Y' or arg == 'Yes' or arg == 'YES':
        return True
    
    #if there is no match
    return default

print(sys.version_info[0])
if sys.version_info[0] < 3:
    python2_rspec_menu
    exit(0)

print("Python Version 3")
print("Select the options that you want for your vulnerable VM.")

RspecCommands = []

#later ask if a person wants to open their own ports
#create OWASP Juice Shop? Default is Yes.
boolVal = getBool(input("Do you want to use the OWASP Juice Shop? (Enter \'y\' for yes or \'n\' for no)."),True)
Item = RspecMenuItem("sudo wget --no-check-certificate -O /local/juice_shop.py https://raw.githubusercontent.com/cawilson1/geniTests/master/juice_shop.py", 
               boolVal)
RspecCommands.append(Item)

#test value. default is No.
boolVal = getBool(input("Test Value? (Enter \'y\' for yes or \'n\' for no)."),False)
Item2 = RspecMenuItem("This is a test",
                boolVal)
RspecCommands.append(Item2)


rspec1 = open("first_half_Rspec.txt",mode='r').read()
#print(rspec1)
rspec2 = open("second_half_Rspec.txt",mode='r').read()
#print(rspec2)
F = open("fullRspec.txt","w")
F.writelines(rspec1)

for MenuItem in RspecCommands:
    if MenuItem.getRspecLines() is not None:
        F.writelines(MenuItem.getRspecLines())
        
F.writelines(rspec2)

print("Finished creating rspec and saved at: ")