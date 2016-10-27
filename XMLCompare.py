#! python2
# XMLCompare.py - compare two XML files

import os,lxml
from lxml import etree
doc = etree.parse('test.xml')

memoryElem = doc.find('LifecycleController.Embedded.1')
#print memoryElem.text ()        # element text
print memoryElem.get('LCAttributes.1#CollectSystemInventoryOnRestart') # attribute