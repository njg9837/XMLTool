#!python3

import re
import window3
from window3 import *


#Open XML files, assign to variables and read contents
xml = open(window3.GUI.bb1())
xml2 = open('test2.xml')
file = xml.readlines()
file2 = xml2.readlines()

#Function to find difference between lists
##########################################
def diff(list1, list2):
    c = set(list1)
    d = set(list2)
    return list(c - d)
##########################################

#Look for <Component FQDD="BIOS.Setup.1-1"> in first file to get begining index
StartIndex = file.index('<Component FQDD="BIOS.Setup.1-1">\r\n')

#Find end of attributes list and get index
for p in file:
    EndIndex = file.index('</Component>\r\n', StartIndex)
print (file[StartIndex:EndIndex])

#Assign data for comparison to attributeList
attributeList = file[StartIndex:EndIndex]

#Look for <Component FQDD="BIOS.Setup.1-1"> in second file to get begining index
StartIndex = file2.index('<Component FQDD="BIOS.Setup.1-1">\r\n')

#Find end of attributes list and get index
for q in file2:
    EndIndex = file2.index('</Component>\r\n', StartIndex)
print (file2[StartIndex:EndIndex])

#Assign data for comparison to attribute
attributeList2 = file2[StartIndex:EndIndex]

#Compares both lists and displays the attribute names that differ
if attributeList != attributeList2:
    print('\nThe following attributes do not match:')
    mismatch = diff(attributeList, attributeList2)
    str = ''.join(mismatch)
    quoted = re.compile('"[^"]*"')
    for value in quoted.findall(str):
        print(value)



