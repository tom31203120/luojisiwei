python 获取罗辑思维每天的微信语音
getContent.py:
#coding=utf-8
import re,urllib2

f = file('luoji.txt', 'w')

def getHtmlCode(url):
    return urllib2.urlopen(url).read()

def getTitle(htmlString):
    regTitle = re.compile("xst\">(.+?) ")
        return regTitle.findall(htmlString)

def getUrl(htmlString):
    regUrl = re.compile("href=\"(.+?)\" onclick=\"atarget\(this\)")
        return regUrl.findall(htmlString)

def getContent(htmlString):
    regContent = re.compile("align=\"left\">(.+?)<br")
        return regContent.findall(htmlString)

def getMp3Url(htmlString):
    regMp3 = re.compile("http(.+?).mp3\'")
        return regMp3.findall(htmlString)

def getLuojiContent(url):
    htmlCode = getHtmlCode(url)
        titles = getTitle(htmlCode)
        urls = getUrl(htmlCode)
        for i in range(0,len(urls)):
            print titles[i]
                f.write(titles[i] + '-')
                contentHtml = getHtmlCode(urls[i])
                contents = getMp3Url(contentHtml)
                if len(contents) > 0:
                    mp3Url = 'http' + contents[0] + '.mp3'
                        print mp3Url
                        f.write(mp3Url + '\n')


if __name__ == '__main__':
    for i in range(1,38):
        print str(i)
            url = 'http://www.ljsw.cc/forum-39-' + str(i) + '.html'
                try:
                    getLuojiContent(url)
                        print 'finished: ' + str(i)
                except:
                    print str(i) + ': error!'
                print '-------------------------------------------------'

downloadMp3.py:
#coding=utf-8
import re,urllib2,os

for line in open("luoji.txt"):
    contents = line.split('-')
        url = line[11:len(line)-1]
        cmd = 'curl -O "%s"' % (url)
        os.system(cmd)
        fileName = url.split('/')
        name = fileName[len(fileName) - 1]
        os.rename(name,contents[0] + '.mp3')
       
        if os.path.getsize(contents[0] + '.mp3') < 100000L:
            url = line[11:len(line)-1]
                cmd = 'curl -O "%s"' % (url)
                os.system(cmd)
                fileName = url.split('/')
                name = fileName[len(fileName) - 1]
                os.rename(name,contents[0] + '.mp3')
combine.py:
from glob import iglob
import shutil
import os

PATH = r'mp3'
destination = open('luoji.mp3', 'wb')
for filename in iglob(os.path.join(PATH, '*.mp3')):
    shutil.copyfileobj(open(filename, 'rb'), destination)
destination.close()
