'''
Created on 2013-3-4

@author: BXC2011032
'''
import urllib

url = "http://www.baidu.com"
ufile = urllib.urlopen(url)  ## get file-like object for url
info = ufile.info()   ## meta-info about the url content
if info.gettype() == 'text/html':
    print 'base url:' + ufile.geturl()
    text = ufile.read()  ## read all its text
    print text