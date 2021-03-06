# -*- coding: utf-8 -*-
import time
import re
import urllib2
import threading
#import android
import HTMLParser
content = urllib2.urlopen('http://www.landho.cn/fax/index.php').read()

def extractData(regex, content, index=1):
    r = '0'
    p = re.compile(regex,re.U|re.S)
    m = p.search(content)
    if m:
        r = m.group(index)
    return r

#采集范围设定
regex = r'<div id="portal_block_651_content" class="dxb_bc">(.*?)<div id="framel9zuNX_right" class="column frame-1-1-1-r">'
newcontent =  extractData(regex, content, 1)

ss=newcontent.replace("","")
urls=re.findall(r"href=.*?title",ss,re.U|re.S)

class MyThread(threading.Thread):
    def __init__(self,threadname):
        threading.Thread.__init__(self,name=threadname)

    def run(self):
        #采集内容页面
        specific = urllib2.urlopen(self.getName()).read()
        #正则获取内容页面标题
        t_regex = r'<title>(.*?)</title>'
        titlecontent =  extractData(t_regex, specific, 1)
        print titlecontent
        filenamearray = self.getName().split('/')
        filetemp =  filenamearray[len(filenamearray)-1]
        filename = filetemp.split('.')
        #print filename[0]
        #正则获取内容页面标题
        c_regex = r'<div class="a_pr"style="margin-left:10px;width:auto">(.*?)<font color="gray">'
        tpcontent =  extractData(c_regex, specific, 1)
        #文件保存
        filetime = time.time()
        file_object = open('file/'+'%s'%filename[0]+'%d'%filetime+'.html','w')
        file_object.writelines(tpcontent)
        file_object.close()
        time.sleep(1)

for i in urls:
   i1 = i.replace('href="','') #过滤替换href="
   i2 = i1.replace('" title','') #过滤替换" title
   my = MyThread(i2)
   my.start()
else:
   print 'this is over'