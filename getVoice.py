#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import urllib2
from bs4 import BeautifulSoup

f = file('home.html', 'w')

home_page = urllib2.urlopen('https://zh.moegirl.org/%E8%88%B0%E9%98%9FCollection').read()
soup_home = BeautifulSoup(home_page, "lxml")
soup_home = soup_home.find_all("td", "navbox-list")
kan_list = BeautifulSoup(str(soup_home), "lxml")
kan_list = kan_list.find_all("a")
#print soup_home
#print str(kan_list)

f.write(str(kan_list))
f.close()
