# -*- coding: utf-8 -*-
import time
import re
import urllib2
#import android
import HTMLParser
content = urllib2.urlopen('http://www.landho.cn/fax/index.php').read()
#filetime = time.time()
#file_object = open('file/'+'%d'%filetime+'.html','w')
#file_object.writelines(content)
#file_object.close()
#print content

#提取<a>标签
#class parseLinks(HTMLParser.HTMLParser):
#    def handle_starttag(self, tag, attrs):
#        if tag == 'a':
#            for name,value in attrs:
#                if name == 'href':
#                    print value
#                    print self.get_starttag_text()
#
#lParser = parseLinks()
#lParser.feed(content)

#正则内容匹配
#def extractData(regex, content, index=1):
#    r = '0'
#    p = re.compile(regex,re.U|re.S)
#    m = p.search(content)
#    if m:
#        r = m.group(index)
#    return r
#
#regex = r'你(.*)朋友'
#content = '我是你的好朋友'
#index = 1
#print extractData(regex, content, index)

def extractData(regex, content, index=1):
    r = '0'
    p = re.compile(regex,re.U|re.S)
    m = p.search(content)
    if m:
        r = m.group(index)
    return r
#portal_block_651_content
regex = r'<div id="portal_block_651_content" class="dxb_bc">(.*?)<div id="framel9zuNX_right" class="column frame-1-1-1-r">'
index = 1
newcontent =  extractData(regex, content, index)

ss=newcontent.replace("","")
#urls=re.findall(r"<a.*?href=.*?<\/a>",ss,re.I)
urls=re.findall(r"href=.*?title",ss,re.U|re.S)
for i in urls:
   i1 = i.replace('href="','')
   i2 = i1.replace('" title','')
   #print i2
   specific = urllib2.urlopen(i2).read()
   t_regex = r'<title>(.*?)</title>'
   index = 1
   titlecontent =  extractData(t_regex, specific, index)
   print titlecontent
else:
   print 'this is over'