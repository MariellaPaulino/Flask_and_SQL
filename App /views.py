# -*- coding: utf-8 -*-

from app import app  # Go get stuff we need from the app folder


@app.route('/')   # This means that this is the view for the landing page.					# 
def index():  
	return ("Hello world!")	# All we are doing is saying Hello!
