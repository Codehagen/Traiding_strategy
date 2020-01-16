from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt



ti = TechIndicators(key='LHFZM9FAGF3J9RV2',output_format='pandas')
data, meta_data = ti.get_bbands(symbol='TSE:TD',interval='1min', time_period=60)
data.plot()
plt.show()


ts = TimeSeries(key='LHFZM9FAGF3J9RV2',output_format='pandas')
data, meta_data = ts.get_intraday(symbol='TSE:TD',interval='60min', outputsize='full')
print(data)
data['4. close'].plot()
plt.title('Intraday TimeSeries Google')
plt.show()

