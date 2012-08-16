#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import odesk
import dbus
import time

USERNAME = 'mindinpanic'
ODESK_PUBLIC_KEY = '025ddd87b98d9db1a53a93cd52b9e89f'
ODESK_SECRET_KEY = '5be81463f3e262c3'

INBOX_URL = 'https://www.odesk.com/api/mc/v1/trays/%s/inbox.json' % USERNAME

def make_noty(title, body):
	knotify = dbus.SessionBus().get_object("org.kde.knotify", "/Notify")
	knotify.event("warning", "kde", [], title, body, [], [], 0, 0, dbus_interface="org.kde.KNotify")

# client = odesk.Client(ODESK_PUBLIC_KEY, ODESK_SECRET_KEY)
# frob = client.auth.get_frob()
# if frob:
# 	print frob
# 	time.sleep(10)
# 	auth_token, user = client.auth.get_token(frob)
# client = odesk.Client(ODESK_PUBLIC_KEY, ODESK_SECRET_KEY, auth_token)

# print client.mc.get_tray_content(USERNAME, 'inbox', paging_offset=0, paging_count=20)

if __name__ == '__main__':
	make_noty(u'test', u'body')