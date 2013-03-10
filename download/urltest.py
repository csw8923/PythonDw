# -*- coding: utf-8 -*-
import time
import re
import urllib2
import threading
#import android
import HTMLParser
content = urllib2.urlopen(' http://www.admin5.com/browse/177/index.shtml ').read()
print content
file_object = open('file/urltest.html','w')
file_object.writelines(content)
file_object.close()