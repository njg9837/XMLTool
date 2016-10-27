#! Python2

import os

file = open('test.xml', 'r')  #Open XML file
allfile = file.readlines()
#print file.readlines()
#print allfile[0]
count = 0
biosIndex = 0
end = 0

for p in allfile:
    count = count + 1                                       #Loop counter
    if '<Component FQDD="BIOS.Setup.1-1">\n' in p:          #Look for <Component FQDD="BIOS.Setup.1-1"> in file
        print p                                             #Print <Component FQDD="BIOS.Setup.1-1">
        print count                                         #Print # of loops (line # of file)
        print allfile[1871]                                 #Print line that matches case
        biosIndex = count                                   #Set biosIndex as counter for attributes
done = 0

while done == 0:
    biosIndex = biosIndex + 1
    print allfile[biosIndex]
    if '</Component>\n' in allfile:
        done = 1
        print allfile[biosIndex:]




#allfile.split = []
#allfile = file
#allfile = allfile.split('\n')
#lifecyclecontroler = []
#for line in file:
    #if "LifecycleController.Embedded.1" in line:
       # lifecyclecontroler.append(line)
        #print(lifecyclecontroler)
        #for line in file:
        #if "CollectSystemInventoryOnRestart" in line:
            #print()

