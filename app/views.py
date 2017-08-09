 #!/usr/local/bin/python
 # -*- coding: utf-8 -*-
from urllib2 import *
import urllib
import sys
import os

from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

reload(sys)
sys.setdefaultencoding('utf-8')



@app.route('/login',methods=['GET', 'POST'])

def login():
	#s='黄金'
	
	#s=s.encode("utf-8")
	form = LoginForm()
	if form.validate_on_submit():
		#s='白银'
		#flash(s)
		s=form.openid.data
		s=s.encode("utf-8")
		k='。'
		k=k.encode("utf-8")
		t=urllib.quote(s)
		#flash(t)
		url='http://localhost:8983/solr/test2/select?q="%s'%(t)+'"&wt=python'
		connection = urlopen(url)
		response = eval(connection.read())
		#flash('Login requested for OpenID="'+form.openid.data +'",remember_me=' +str(form.remember_me.data))
		#return redirect('/')
		#flash(s)
		i=1
		j=250
		# flash(str(response['response']['numFound'])+' result(s) found.')

		flash(form.openid.data)
		for document in response['response']['docs']:
			flash(str(i)+' '+document['title'])
			#flash(document['title'])
			if len(document['content'])<300:
				flash(document['content']) 
			else:
				#flash(document['content'][0:300]) 
				while (j<300):
					if document['content'][j]==k:
						flash(document['content'][0:j+1])	
						break
					j=j+1
			j=200
			i=i+1
	return render_template('login.html',title='Search',  form = form, providers = app.config['OPENID_PROVIDERS'])

@app.route('/')
@app.route('/index')
def index():
	user={'nickname':'Bro Qingyang'} # fake user
	posts = [
	{
		'author':{'nickname':'John'},
		'body':'The Avengers movie was so cool!'
	},
	{
		'author':{'nickname':'Susan'},
		'body':'Beautiful day in Portland!'
	}
	]
	
	return render_template("index.html",title='Home',user = user,posts = posts)