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
    def getRspecLines(self):
        #if true, we want to add this line of code to execute for the rspec
        if self.run:
            return ('<execute xmlns=\"http://www.geni.net/resources/rspec/3\" command=\"' + self.cmd + '\" shell=\"/bin/sh\"/>')
        
        
#put line library here for the lines to use for a given vulnerable addition