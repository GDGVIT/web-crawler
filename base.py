from Tkinter import *
from bs4 import BeautifulSoup
import HTMLParser
import urllib
import os
import re
from urlparse import urljoin
root = Tk()
l1 = Label(root)
l2 = Label(root)
e1 = Entry(root)
e2 = Entry(root)
l = Label(root)
l1.config(text = "url")
l2.config(text = "path")
def callback():
    urlInput = e1.get()
    path=e2.get()
    print urlInput
    print path
    html = urllib.urlopen(urlInput).read()
    soup = BeautifulSoup(html)
    tags = soup('a')    
    urls = set()
    finalUrls=set()
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
            script(url,path)
            css(url,path)
            print "\n"
        except:
            print 'none'

def script(url,path):
    Folder=url.replace('http://',"")
    subFolder=os.path.join(path+"/"+Folder)
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
def css(url,path):
    Folder=url.replace('http://',"")
    subFolder=os.path.join(path+"/"+Folder)
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
b = Button(root, text="extrack", command=callback)
for widget in (l1,e1,l2, e2, l, b):
    widget.pack()
b.mainloop()
