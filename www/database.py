from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Samples

import os

class Database(object):
    session = None
    db_user = os.getenv("DB_USER") if os.getenv("DB_USER") != None else "root"
    db_pass = os.getenv("DB_PASS") if os.getenv("DB_PASS") != None else "root"
    db_host = os.getenv("DB_HOST") if os.getenv("DB_HOST") != None else "127.0.0.1"
    db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else "samples"
    db_port = os.getenv("DB_PORT") if os.getenv("DB_PORT") != None else "3306"
    Base = declarative_base()
    
    def get_session(self):
        """Singleton of db connection

        Returns:
            [db connection] -- [Singleton of db connection]
        """
        if self.session == None:
            connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
            engine = create_engine(connection,echo=True)
            connection = engine.connect()
            Session = sessionmaker(bind=engine)
            self.session = Session()
            self.Base.metadata.create_all(engine)
        return self.session

    def save_values(self, values):
        session = self.get_session()
        samp = Samples(temperature=values['measuredtemp'],humidity=values['measuredhum'],pressure=values['measuredpres'],windspeed=values['measuredwsp'])
        session.add(samp)
        session.commit()
        id = int(samp.id)
        session.close()
        return str(id)

    def get_data(self):
        session = self.get_session()
        last_sample = session.query(Samples).order_by(Samples.id.desc()).first()
        session.close()
        return last_sample

    def get_temp_avg(self):
        session = self.get_session()
        temp_avg = session.query(func.avg(Samples.temperature)).order_by(Samples.id.desc()).all()[:10]
        session.close()
        return temp_avg[0]

    def get_hum_avg(self):
        session = self.get_session()
        hum_avg = session.query(func.avg(Samples.humidity)).order_by(Samples.id.desc()).all()[:10]
        session.close()
        return hum_avg[0]

    def get_wind_avg(self):
        session = self.get_session()
        wind_avg = session.query(func.avg(Samples.windspeed)).order_by(Samples.id.desc()).all()[:10]
        session.close()
        return wind_avg[0]

    def get_press_avg(self):
        session = self.get_session()
        press_avg = session.query(func.avg(Samples.pressure)).order_by(Samples.id.desc()).all()[:10]
        session.close()
        return press_avg[0]

    def get_all_avg(self):
        session = self.get_session()
        temp_avg = session.query(func.avg(Samples.temperature)).order_by(Samples.id.desc()).all()[:10]
        hum_avg = session.query(func.avg(Samples.humidity)).order_by(Samples.id.desc()).all()[:10]
        wind_avg = session.query(func.avg(Samples.windspeed)).order_by(Samples.id.desc()).all()[:10]
        press_avg = session.query(func.avg(Samples.pressure)).order_by(Samples.id.desc()).all()[:10]
        avg_values = {}
        avg_values['avgtemp'] = str(temp_avg[0][0])
        avg_values['avghum'] = str(hum_avg[0][0])
        avg_values['avgpres'] = str(press_avg[0][0])
        avg_values['avgwsp'] = str(wind_avg[0][0])
        session.close()
        return avg_values