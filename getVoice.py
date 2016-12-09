#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import urllib2
from bs4 import BeautifulSoup
from urlparse import urljoin
import re

f = file('home.html', 'w+')

name_list = ""

home_page = urllib2.urlopen('https://zh.moegirl.org/%E8%88%B0%E9%98%9FCollection').read()
soup_home = BeautifulSoup(home_page, "lxml")
soup_home = soup_home.find_all("td", "navbox-list")
kan_list = BeautifulSoup(str(soup_home), "lxml")
kan_list = kan_list.find_all("a")

kan_list_str = str(kan_list)
kan_list_str = re.sub(u"\,", "", kan_list_str)
kan_list_str = re.sub(u"\[", "", kan_list_str)
kan_list_str = re.sub(u"\]", "", kan_list_str)
kan_list_str = re.sub(u"> <", "><", kan_list_str)

for link in BeautifulSoup(str(kan_list_str), "lxml").body.children: 
 #print type(link)
 name_list = name_list + "https://zh.moegirl.org" + link['href'] + "\n"
print name_list

f.write(name_list)

f.close()
