#!/usr/bin/python3
from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def index():
	return 'Hello !'

@app.route('/<path:file>')
def file(file):
	return open(file).read()

app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
# debug=True옵션을 사용하면 어떠한 에러가 발생하면 에러를 보여주는 페이지가 나온다. 
# 해당 페이지에서 콘솔을 실행할 수 있다. 근데 콘솔을 실행시키려면 pin이 필요하다.
