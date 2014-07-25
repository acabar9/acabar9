from flask import render_template, Flask, request
from apps import app


@app.route('/')
	return render_template("index.html")
@app.route('/calc', methods=['POST'])
def calc():
	a= request.form ["text_get_a"]
	b= request.form ["text_get_b"]
	c= int(a)+int(b)
	return render_template("result.html", val_result=c)