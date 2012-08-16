#!/usr/bin/env python
# -*- coding: utf-8 -*-

d='http://paste.pocoo.org/show/559871'

from grab import Grab
import sys, os, pprint
#from PyQt4.QtGui import QApplication
#from PyQt4.QtWebKit import QWebView
#from PyQt4.QtCore import QUrl, QObject, SIGNAL
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.QtNetwork import *
from time import sleep
import pickle


pages_count = 10
urls = [u'http://kievskaya.emarket.ua/biznes-i-uslugi/stroitelstvo-remont/kyiv/']
urls.extend([urls[0] + u'?search[page]=%d#page' % i for i in range(2,pages_count) ])
js_click = u'$(".link-spoiler-show").click()'
phone_xpath = u'/html/body/div/div[2]/div/div/div/div/div[5]/div/div/div/ul/li/div[2]/strong'


stickers_links_pck = 'links_%d.pck' % pages_count

if not os.path.exists(stickers_links_pck):
    stickers_links = []
    for url in urls:
        g = Grab()
        g.go(url)
        for i in g.xpath_list('//h4[@class="normal"]/a[@class="link"]'):
            title, href = i.get('title'), i.get('href')
            if title and href: stickers_links.append((title, href))
    f=open(stickers_links_pck, 'wb')
    pickle.dump(stickers_links, f)
    f.close()
    

f=open(stickers_links_pck, 'rb')
links = pickle.load(f)
f.close()
phones = []

get_phone = lambda g: g.xpath_text(phone_xpath)
get_html = lambda view: str(view.page().mainFrame().toHtml().toUtf8())

app = QApplication(sys.argv)
view = QWebView()
g=Grab()


for title, link in links[:1]:
    #view.setHtml(g.go(link).body)
    
    def _on_load(i):
        print 'here' 
    
    #page = view.page()
    #app.connect(view, SIGNAL("loadFinished(bool)"), _on_load)
    view.load(QUrl(link))
    
    #try:
    #    frame = view.page().mainFrame()
    #    frame.evaluateJavaScript(js_click)
    #    print get_html(view)
        #g.response.body = get_html(view)
        #p=get_phone(g)
        #phones.append((title, p))
    #except Exception as e:
    #    print e
    #    print link
    #    print h

pprint.pprint(phones)
