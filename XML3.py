#!/usr/bin/python2.7

import os

file = open('test.xml', 'r')
file2 = open('test2.xml','r')
allfile = file.readlines()

BiosIndex = allfile.index('<Component FQDD="BIOS.Setup.1-1">\r\n')
print(BiosIndex)

for p in allfile:
    EndBiosIndex = allfile.index('</Component>\r\n',BiosIndex)
print(EndBiosIndex)
print allfile[BiosIndex:EndBiosIndex]
BiosAtt = allfile[BiosIndex:EndBiosIndex]

comparefile = file2.readlines()
BiosIndex = comparefile.index('<Component FQDD="BIOS.Setup.1-1">\r\n')

for q in comparefile:
    EndBiosIndex = comparefile.index('</Component>\r\n',BiosIndex)
print comparefile[BiosIndex:EndBiosIndex]
BiosCompare = comparefile[BiosIndex:EndBiosIndex]

diff = list(set(BiosAtt) - set(BiosCompare))
print (diff)
