import schedule
import time

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

print("Updating stocks...")

#Your Key
key = 'LHFZM9FAGF3J9RV2'

def AlphaVantage(symbol):
    ts = TimeSeries(key, output_format='pandas')
    data = ts.get_intraday(symbol, interval='5min', outputsize='full')
    #Chart
    

    print(str(data))
    print("Updating stocks...10 seconds to next update")

#What Stock
AlphaVantage('AMD')






#Timer on updates
schedule.every(10).seconds.do(AlphaVantage, symbol='AMD')

while 1:
   schedule.run_pending()
   time.sleep(1)