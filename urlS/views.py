from urlS import app
from flask import render_template, request


@app.route('/')
@app.route('/index')
#these include the data itself that could be part of the view. The html page controls how it looks and what gets shown

def index():
	return render_template("index.html")

@app.route('/shortened')
def shortened():
	theUrl=request.args.get("url","")
	return render_template("shortened.html", url=theUrl)