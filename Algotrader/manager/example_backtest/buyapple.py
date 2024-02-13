from zipline.api import order, record, symbol
#used for creating plots and visualizations
import matplotlib.pyplot as plt 

#function definition that takes in context, a dictionary where you can store and access variables through the trading session
def initialize(context):
	#function is empty
    pass


def handle_data(context, data):
	#buy 10 shares of apple stock
    order(symbol('AAPL'), 10)
	#record the current price of Apple stock
    record(AAPL=data[symbol('AAPL')].price)

"""
def analyze(context, perf):
	ax1 = plt.subplot(211)
	perf.portfolio_value.plot(ax=ax1)
	ax1.set_ylabel('portfolio value')
	ax2 = plt.subplot(212, sharex=ax1)
	perf.AAPL.plot(ax=ax2)
	ax2.set_ylabel('AAPL stock price')
	plt.show()

"""
