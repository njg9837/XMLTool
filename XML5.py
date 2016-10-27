#!python2

import re

#Open XML files, assign to variables and read contents
file = open('test.xml').readlines()
file2 = open('test2.xml').readlines()

def biosIndex(component):
    #Look for <Component FQDD="BIOS.Setup.1-1"> in first file to get begining index

    start_index = component.index('<Component FQDD="BIOS.Setup.1-1">\r\n')
    end_index = component.index('</Component>\r\n', start_index)
    #Find end of attributes list and get index
    #for p in component:
        #try:
           #end_index = component.index('</Component>\n', start_index)
            #attribute_list = file[start_index:end_index]

        #Assign data for comparison to attribute_list
        #except:
            #print "Error!"
    return component[start_index:end_index]

att1 = biosIndex(file)
att2 = biosIndex(file2)
print att1
print att2


#Find difference between lists
def diff(list1, list2):
    c = set(list1)
    d = set(list2)
    return list(c - d)


#Compares both lists and displays the attribute names that differ
def compare(att1, att2):
    if att1 != att2:
        print('\nThe following attributes do not match:')
        mismatch = diff(att1,att2)
        str = ''.join(mismatch)
        quoted = re.compile('"[^"]*"')
        for value in quoted.findall(str):
            print(value)

compare(att1,att2)

