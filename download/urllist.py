# -*- coding: utf-8 -*-
import time
import re
import urllib2
import threading
#import android
import HTMLParser
content = urllib2.urlopen(' http://www.admin5.com/browse/177/index.shtml ').read()
def extractData(regex, content, index=1):
    r = '0'
    p = re.compile(regex,re.U|re.S)
    m = p.search(content)
    if m:
        r = m.group(index)
    return r
    
#采集范围设定
regex = r'<ul class="list">(.*?)</ul>'
newcontent =  extractData(regex, content, 1)
print newcontent
file_object = open('file/urllist.html','w')
file_object.writelines(newcontent)