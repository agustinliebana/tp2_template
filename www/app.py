# Imports
from aux_pro import Process
from flask import Flask
from flask import render_template, jsonify
from database import Database

app = Flask(__name__)
db = Database()
proc = Process()


@app.route('/')
def index():
    return render_template('index.html', temp=db.get_temp_avg()[0])

@app.route('/refresh', methods=['GET'])
def refresh():

    last_sample = db.get_data()
    return jsonify(temperature=last_sample.temperature,
                   humidity=last_sample.humidity,
                   pressure=last_sample.pressure,
                   windspeed=last_sample.windspeed)


@app.route('/measures', methods = ["GET"])
def get_sample():
  sample = db.get_data()
  return jsonify(sample)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
