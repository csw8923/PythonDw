#-*- coding:utf-8 -*-
import sys
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

def do_some(a,t):
    content = urllib2.urlopen(a).read()
    #采集范围设定
    regex = r'<ul class="list">(.*?)</ul>'
    newcontent =  extractData(regex, content, 1)
    return t+newcontent
    #return "dosome:%s" % a
if __name__ == '__main__':
    url = sys.argv[1]
    t = sys.argv[2]
if url:
    #T = do_some(url,t)
#print T
    print url