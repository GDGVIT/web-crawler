#from bs4 import BeautifulSoup
#import urllib
#from urlparse import urljoin

#url = raw_input('enter - ')
#html = urllib.urlopen(url).read()
#soup = BeautifulSoup(html)
#tags = soup('a')

#for tag in tags:
#    print tag.get('href')

#for tag in tags:
#     (urljoin(url, tag.get('href')))
#link=soup.find_all('a')
#script=soup.find_all('script')
#print script
#css=soup.find_all("link")
#print css
#link=soup.find_all('href')
#print link
from bs4 import BeautifulSoup
import HTMLParser
import urllib
import os
import re
from urlparse import urljoin
def script(url):
    subFolder=url.replace('http://',"")
    if not os.path.exists(subFolder):
        os.makedirs(subFolder)
    completeName=os.path.join(subFolder+"/SCRIPT.txt")
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    fo=open(completeName,'w+')
    fo.seek(0)
    fo.truncate()
    scripts=soup.find_all('script')
    for tag in scripts:
        try:
            File = tag["src"]
            fo.write(File+"\n")
        except:
            print "no source"
'''    else:
        completeName=os.path.join(str(subFolder)+"/script.txt")
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        fo=open(completeName,'w+')
        scripts=soup.find_all('script')
        for tag in scripts:
            try:
                File = tag["src"]
                fo.write(File+"\n")
            except:
                print tag
        fo.close()'''

def css(url):
    subFolder=url.replace('http://',"")
    if not os.path.exists(subFolder):
        os.makedirs(subFolder)
    completeName=os.path.join(subFolder+"/CSS.txt")
    fo=open(completeName,'w+')
    fo.seek(0)
    fo.truncate()
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    css=soup.find_all('link')
    for tag in css:
        try:
            File = tag["href"]
            fo.write(File+"\n")
        except:
            print "no source"
'''    else:
        completeName=os.path.join(subFolder+"/CSS.txt")
        html = urllib.urlopen(url).read()
        soup = BeautifulSoup(html)
        css=soup.find_all('link')
        for tag in css:
            try:
                File = tag["herf"]
                fo.write(File+"\n")
            except:
                print tag
    
'''
urlInput = raw_input('enter - ')
html = urllib.urlopen(urlInput).read()
soup = BeautifulSoup(html)
tags = soup('a')    
urls = set()
finalUrls=set()
#folderName=urlInput.lstrip("http://")
#print folderName
#path=folderName
#if not os.path.exists(path):
#    os.makedirs(path)
try:
    script(urlInput)
    css(urlInput)
except:
    print 'none'
for tag in tags:
    urls.add(urljoin(urlInput, tag.get('href')))

for url in urls:
     if re.match(urlInput,url):
         finalUrls.add(url)
for url in finalUrls:
    print url
    try:
        script(url)
        css(url)
        print "\n"
    except:
        print 'none'
