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

