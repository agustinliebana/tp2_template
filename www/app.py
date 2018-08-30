# Imports
from flask import Flask
from flask import render_template , request, jsonify
from database import Database

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/refresh', methods=['POST'])
def refresh():

    update_int = request.form['interval']

    last_sample = Database().get_data()
    

    return jsonify({'temperature' :})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

