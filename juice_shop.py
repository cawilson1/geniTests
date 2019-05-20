# -*- coding: utf-8 -*-
"""
Created on Mon May 20 09:25:59 2019

@author: User
"""
import os

def juiceShop():
    #juice-shop setup and run
    os.system("curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -")
    os.system("sudo apt-get install -y nodejs")
    os.system("wget https://github.com/bkimminich/juice-shop/releases/download/v8.4.1/juice-shop-8.4.1_node10_linux_x64.tgz")
    os.system("tar -xzvf juice-shop-8.4.1_node10_linux_x64.tgz")
    os.system("cd juice-shop_8.4.1 && sudo npm start")

