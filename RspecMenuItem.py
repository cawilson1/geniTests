# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:23:40 2019

@author: User
"""

class RspecMenuItem:
    def __init__(self, cmd, run=False):
        self.cmd = cmd
        self.run = run
        
    def printAll(self):
        print(self.cmd)
        print(self.run)
        
    #return relevant lines for Item
    #client should add specific lines
    def getRspecLines(self):
        strList = []#list of strings to concat
        #if true, we want to add this line of code to execute for the rspec
        if self.run:
            strList.append('<execute xmlns=\"http://www.geni.net/resources/rspec/3\" command=\"' + self.cmd + '\" shell=\"/bin/sh\"/>')
            strList.append('<execute xmlns=\"http://www.geni.net/resources/rspec/3\" command=\"sudo python /local/' + self.cmd.rsplit('/',1)[-1] + '\" shell=\"/bin/sh\"/>')
            return ''.join(strList)
        
#put line library here for the lines to use for a given vulnerable addition