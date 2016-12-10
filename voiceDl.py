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

def dlMp3(mp3_list, url):
 dl_log =""
 list_name_code = ""
 if mp3_list:
  if url.split('%E8%88%B0%E9%98%9FCollection:')[-1] != url:
   fir_title = url.split('%E8%88%B0%E9%98%9FCollection:')[-1]
   if mkdir("voice/" + fir_title):
    print urllib.unquote(fir_title)
    dl_log = dl_log + urllib.unquote(fir_title) + "\n"
    list_name_code = fir_title + " " + urllib.unquote(fir_title) 
    for mp3_url in mp3_list:
     title = "voice/" + fir_title + "/" + mp3_url.split('/')[-1]
     path = os.path.join(main_path, title)
     urllib.urlretrieve(mp3_url, path)
     print '|-' + title
     dl_log = dl_log + '|-' + title + "\n"
 return dl_log, list_name_code

def mkdir(title):
 if title != "":
  title = title.strip()
  isExists = os.path.exists(title)
  if not isExists:
   os.makedirs(title)
   os.chmod(title, 777)
   return True
  else:
   print "Exit: " + title 
   return False else:
  print "Empty title!" 
  return False
     
# url1 = "https://zh.moegirl.org/%E8%88%B0%E9%98%9FCollection:%E9%87%91%E5%88%9A"
# url2 = "https://zh.moegirl.org/%E8%88%B0%E9%98%9FCollection:%E9%95%BF%E9%97%A8"
# url3 = "https://zh.moegirl.org/%E9%AB%98%E6%A0%A1%E8%88%B0%E9%98%9F"
# url = "https://zh.moegirl.org/%E8%88%B0%E9%98%9FCollection:%E6%95%8C%E8%88%B0%E8%BD%BD%E6%9C%BA"
#print main_path
f = file('dl.log', 'w+')
f2 = file('name.ls', 'w+')
url_list = file('tt.html', 'r')
while 1:
    line = url_list.readline()
    if not line:
        break
    if line.split('%E8%88%B0%E9%98%9FCollection:')[-1] != line:
        line = line.strip('\n')
        _output = dlMp3(getMp3(line), line)
        f.write(_output[0])
        f2.write(_output[1])
        print line.split('%E8%88%B0%E9%98%9FCollection:')[-1] + "|" + line
    else:
        print "Error url;"
# f.write(dlMp3(getMp3(url), url))
# f.write(dlMp3(getMp3(url2), url2))
# f.write(dlMp3(getMp3(url3), url3))
f.close()
f2.close()
url_list.close()


#print getMp3(url)

#print urllib.unquote(url)
