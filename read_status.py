#!/usr/bin/python

import json,sys
import requests


def connect_i_net():

	payload = {':sys:HomePlug.Local.Device{Index=1}.Commands.AddRemote':'XYOC-PQMN-ITTL-XZIO',
	'_okdir':'spec',
	'_okpage':'result',
	'_okfollowdir':'status',
	'_okfollowpage':'homeplug',
	'_okplain':'1',
	'_oktype':'dlanstatus',
	'_file':'/wgl/main.wgl',
	'_style':'std',
	'_lang':'de',
	'_dir':'status',
	'_page':'homeplug_add',
	'_idx':'',
	'_sid':'',
	'_csrf':''}

	#print(payload)

	r = requests.post("http://192.168.178.23/cgi-bin/htmlmgr", data=payload)
	#print(r.text)


r = requests.get('http://192.168.178.23/cgi-bin/htmlmgr?_file=getjson&service=hpdevices')

data=r.json()[:-1]#cut last -> row onley empty

i_net = False
for row in data:

	if row['ustr']=='internet':
		i_net = True


if not i_net:
	print ("i-net: disconnected")
	connect_i_net()
	print ("send reconnection request")



