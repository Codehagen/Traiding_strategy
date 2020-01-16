import schedule
import time

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

print("Updating stocks...")
#Din key fra alpha
key = 'LHFZM9FAGF3J9RV2'

def AlphaVantage(symbol):
    ts = TimeSeries(key)
    data = ts.get_intraday(symbol, interval='1min')

    print(str(data))

 #Skriv inn hvordan aksje du vil ha
AlphaVantage('AMD')

def job():
   print("I'm working...")



#Timer på updates
schedule.every(1).seconds.do(job)

while 1:
   schedule.run_pending()
   time.sleep(1)