from database import Database

import random
import time
import signal

class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True

def main(session):
    killer = GracefulKiller()
    t_seed = random.randint(0, 35)
    h_seed = random.randint(10, 90)
    p_seed = random.randint(900, 1050)
    w_seed = random.randint(0, 50)
    while(1):
        temp = t_seed + random.randint(-5, 5)
        hum = h_seed + random.randint(-5, 5)
        press = p_seed + random.randint(-5, 5)
        windsp = w_seed + random.randint(-5, 5)
        print("***Temperatura: %s \n***Humedad: %s\n***Presion Atmosferica: %s\n***Velocidad del Viento: %s" % (temp, hum, press, windsp))
        values = {}
        values['measuredtemp'] = temp
        values['measuredhum'] = hum
        values['measuredpres'] = press
        values['measuredwsp'] = windsp
        measure_id = db.save_values(values)
        print("***ID de la medida guardada: %s" % measure_id)
        print("***PROMEDIO de la temperatura guardada: %s" % db.get_temp_avg())
        print("***PROMEDIO de la humedad guardada: %s" % db.get_hum_avg())
        time.sleep(1)
        if killer.kill_now:
            session.close()
            break

if __name__ == '__main__':
    db = Database()
    session = db.get_session()
    main(session)