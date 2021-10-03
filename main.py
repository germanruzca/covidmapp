# German Ruiz to the NASA Space Challenge
# Octubre 2021
# @germanruzca

import pickle
from flask import *
import pickle
from calculateLast import calculate24hrs

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/datos/', methods=['GET'])
def request_page():
  population = str(request.args.get('population'))
  weather = str(request.args.get('weather'))
  hour= str(request.args.get('hour'))
  place = str(request.args.get('place'))
  day = str(request.args.get('day'))
  state = str(request.args.get('state'))


  last = calculate24hrs(state)
  prediction = model.predict([[population, weather,hour,  place, day, last]])
  data_set = {
    'name': 'COVID Calulate Places',
    'message': 'data',
    'population': f'{population}',
    'weather': f'{weather}',
    'hour': f'{hour}',
    'place': f'{place}',
    'day': f'{day}',
    'last':f'{last}',
    'state': f'state de {state}',
    'prediccion': f'{prediction}'
  }
  
  return jsonify(data=data_set), 200

if __name__ == '__main__':
  app.run()
