 #!/usr/local/bin/python
 # -*- coding: utf-8 -*-
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

s1='REITS'
s2='中信集团'
s3='做空机制'
OPENID_PROVIDERS = [
	{'name':s1,'url':s1},
	{'name':s2.encode("utf-8"),'url':s2.encode("utf-8")},
	{'name':s3.encode("utf-8"),'url':s3.encode("utf-8")}]
	#{'name':'Flickr','url':'https://www.flickr.com/<username>'}, 
	#{'name':'MyOpenID','url':'https://www.myopenid.com'}