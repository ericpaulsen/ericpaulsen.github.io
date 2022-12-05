from flask import Flask, current_app
import os
app = Flask(__name__)

@app.route('/')
def home():
    return current_app.send_static_file('index.html')

app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))