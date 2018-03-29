'''
Created on 27 Mar 2018

@author: karunanv
'''
from _ast import Param
import os

def joinStrings(s,l,toks):
    """Join string split over multiple lines"""
    return ["".join(toks)]

class extractPaths(object):
    '''
    classdocs
    '''
    homePath = ""
    implPath = ""
    applPath = ""
    bswPath = ""
    glbPath = ""
    libPath = ""
    skltPath = ""
        

    def __init__(self, __homePath__):
        '''
        Constructor
        '''
        self.homePath = __homePath__
        self.implPath = (self.homePath + "\\02_implementation")
        self.applPath = self.implPath + str("\\appl")
        self.bswPath = self.implPath + str("\\bsw")
        self.glbPath = self.implPath + str("\\global")
        self.libPath = self.implPath + str("\\lib")
        self.skltPath = self.implPath + str("\\skeleton")
        
        print(self.homePath)
        print(self.implPath)
        print(self.applPath)
        print(self.bswPath)
        print(self.glbPath)
        print(self.libPath)
        print(self.skltPath)
     
        
    