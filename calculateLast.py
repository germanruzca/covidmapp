# German Ruiz to the NASA Space Challenge
# Octubre 2021
# @germanruzca


from datetime import datetime, timedelta
import pandas as pd


def calculate24hrs(state):
  # Main url raw 
  url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'

  # Get the data of the days and the format
  one_day = datetime.now()- timedelta(1)
  one_day = one_day.strftime('%m-%d-%Y')
  two_day = datetime.now()- timedelta(2)
  two_day = two_day.strftime('%m-%d-%Y')

  # Get the datasets
  newData = pd.read_csv(f'{url}{one_day}.csv')
  oldData = pd.read_csv(f'{url}{two_day}.csv')


  # Get the state to load the specific data
  newData= newData[newData['Province_State']==state]
  oldData= oldData[oldData['Province_State']==state]


# Do maths to get the final cases 
  total = (newData.Confirmed.sum())-(oldData.Confirmed.sum())

  if total > 5000:
    return 10
  elif total > 4500:
    return 9
  elif total > 4000:
    return 8
  elif total > 3500:
    return 7
  elif total > 3000:
    return 6
  elif total > 2500:
    return 5
  elif total > 2000:
    return 4
  elif total > 1500:
    return 3
  elif total > 1000:
    return 2
  elif total > 500:
    return 1
  else: 
    return 0