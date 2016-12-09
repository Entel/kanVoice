#coding=utf-8

import urllib
import re
import os

main_path = os.getcwd()

def getMp3(url):
 page = urllib.urlopen(url)
 html = page.read()
 
 reg = r'href="(.+?\.mp3)"'
 mp3_re = re.compile(reg)
 mp3_list = re.findall(mp3_re, html)
 
 return mp3_list

def dlMp3(mp3_list):
 mkdir("voice/kongo")
 
 for mp3_url in mp3_list:
  title = "voice/kongo/" + mp3_url.split('/')[-1]
  path = os.path.join(main_path, title)
  urllib.urlretrieve(mp3_url, path)
  print title

def mkdir(title):
 title = title.strip()
 isExists = os.path.exists(title)
 if not isExists:
  os.makedirs(title)
  os.chmod(title, 777)
  return True
 else:
  return False


url = "https://zh.moegirl.org/%E8%88%B0%E9%98%9FCollection:%E9%87%91%E5%88%9A"
#print main_path

#dlMp3(getMp3(url))

print getMp3(url)
