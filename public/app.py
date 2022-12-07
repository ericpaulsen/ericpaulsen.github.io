from flask import Flask, render_template, make_response
import os
import time

app = Flask(__name__, static_folder='static')

def format_server_time():
  server_time = time.localtime()
  return time.strftime("%I:%M:%S %p", server_time)

@app.route('/')
def home():
    context = { 'server_time': format_server_time() }
    template = render_template('index.html', context=context)
    response = make_response(template)
    # use shared caches & set freshness to 1 week
    response.headers['Cache-Control'] = 'public, max-age=604800, s-maxage=604800'
    return response

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))