from pytz import timezone
import light_new
import advanced_motion_detector as adm
import random
import face_recongnition
from datetime import datetime

TIMEZONE = timezone('America/New_York')
#data_dict={'num_people':0,'light':0,'motion':0,'time':0}

def get_sensor_readings():
  
    
      motion=str(adm.get_motion())
      #num_people= str(random.randint(1,200))
      num_people = str(random.randint(1,100) * face_recongnition.num_of_people());
      light=str(light_new.a.read())
      time=datetime.now(TIMEZONE).strftime('%H')
      data = {'number of people':num_people,'light':light,'motion':motion,'time':time}
      return data

#f=get_sensor_readings()
#print(f)
