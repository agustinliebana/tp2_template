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
    last_sample = Database().get_data()
    avg_values = Database().get_all_avg()
    return render_template('index.html',temperature=last_sample.temperature,
                   humidity=last_sample.humidity,
                   pressure=last_sample.pressure,
                   windspeed=last_sample.windspeed,
                   tmpavg=avg_values['avgtemp'],
                   preavg=avg_values['avgpres'],
                   humavg=avg_values['avghum'],
                   winavg=avg_values['avgwsp'])

@app.route('/refresh', methods=['GET'])
def refresh():
    last_sample = Database().get_data()
    avg_values = Database().get_all_avg()
    return jsonify(temperature=last_sample.temperature,
                   humidity=last_sample.humidity,
                   pressure=last_sample.pressure,
                   windspeed=last_sample.windspeed,
                   tmpavg=avg_values['avgtemp'],
                   preavg=avg_values['avgpres'],
                   humavg=avg_values['avghum'],
                   winavg=avg_values['avgwsp'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

