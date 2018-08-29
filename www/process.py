from database import Database

import random
import time

def main(session):
    while(1):
        temp = random.randint(0,50)
        hum = random.randint(0,100)
        press = random.randint(900,1050)
        windsp = random.randint(0,100)
        print("Temperatura: " + str(temp) + "\n Humedad:" + str(hum) + "\n Presion Atmosferica: " + str(press) + "\n Velocidad del Viento: " + str(windsp) + "\n")
        values = {}
        values['measuredtemp'] = temp
        values['measuredhum'] = hum
        values['measuredpres'] = press
        values['measuredwsp'] = windsp
        measure_id = db.save_values(values)
        print("ID de la medida guardada: " + str(measure_id))
        time.sleep(1)



if __name__ == '__main__':
    db = Database()
    session = db.get_session()
    main(session)