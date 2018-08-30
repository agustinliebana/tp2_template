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
    tmp_avg = str(Database().get_temp_avg()[0])
    pre_avg = str(Database().get_press_avg()[0])
    hum_avg = str(Database().get_hum_avg()[0])
    win_avg = str(Database().get_wind_avg()[0])
    return jsonify(temperature=last_sample.temperature,
                   humidity=last_sample.humidity,
                   pressure=last_sample.pressure,
                   windspeed=last_sample.windspeed,
                   tmpavg=tmp_avg,
                   preavg=pre_avg,
                   humavg=hum_avg,
                   winavg=win_avg)

@app.route('/upload', methods=['POST'])
def upload_data():
    data = request.form
    values = {}
    values['measuredtemp'] = data['temperature']
    values['measuredhum'] = data['humidity']
    values['measuredpres'] = data['pressure']
    values['measuredwsp'] = data['windspeed']
    return Database().save_values(values)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

