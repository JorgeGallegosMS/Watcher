import os
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

host = os.environ.get('MONGODB_URI')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()




@app.route('/')
def index():
    return render_template('index.html.j2')

if __name__ == '__main__':
    app.run(debug=True)