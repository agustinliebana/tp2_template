# Imports
from flask import Flask
from flask import render_template , request, jsonify
from database import Database
from aux_pro import Process

app = Flask(__name__)
proc = Process()

@app.route('/')
def index():
    proc.start_process()
    return render_template('index.html')

@app.route('/refresh', methods=['GET'])
def refresh():

    last_sample = Database().get_data()
    return jsonify(temperature=last_sample.temperature,
                   humidity=last_sample.humidity,
                   pressure=last_sample.pressure,
                   windspeed=last_sample.windspeed)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

