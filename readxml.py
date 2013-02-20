# -*- coding: utf-8 -*-
import android
from xml.dom import minidom
b = minidom.parse('ip.xml')
for i in b.childNodes[0].getElementsByTagName('p'):
   print i.childNodes[0].toxml()
for i in b.childNodes[0].getElementsByTagName('t'):
   print i.childNodes[0].toxml()