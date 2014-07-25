from flask import render_template, Flask, request
from apps import app


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	get = None
	post = None

	if request.args:
		get = request.args['text_get']

	if request.form:
		post = request.form['text_post']	
	return render_template ("index.html", variable_get = get, variable_post=post)

@app.route('/search', methods=['GET', 'POST'])
def search():
	url="https://www.google.co.kr/#newwindow=1&q="
	url=url+request.args['text_get']
	return render_template ("index.html", variable_get = url)