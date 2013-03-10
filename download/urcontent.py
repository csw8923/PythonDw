# -*- coding: utf-8 -*-
import time
import re
import urllib2
import threading
#import android
import HTMLParser

def extractData(regex, content, index=1):
    r = '0'
    p = re.compile(regex,re.U|re.S)
    m = p.search(content)
    if m:
        r = m.group(index)
    return r

url = 'http://www.admin5.com/article/20130309/491269.shtml';
#采集内容页面
specific = urllib2.urlopen(url).read()
#正则获取内容页面标题
t_regex = r'<title>(.*?)</title>'
titlecontent =  extractData(t_regex, specific, 1)
print titlecontent
filenamearray = url.split('/')
filetemp =  filenamearray[len(filenamearray)-1]
filename = filetemp.split('.')
#print filename[0]
#正则获取内容页面标题
c_regex = r'<div class="content">(.*?)</div>'
tpcontent =  extractData(c_regex, specific, 1)
print tpcontent
file_object = open('file/urlcontent.html','w')
file_object.writelines(tpcontent)
file_object.close()