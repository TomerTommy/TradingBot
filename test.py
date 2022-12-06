# Test connection
'''
from ibapi.client import EClient
from ibapi.wrapper import EWrapper

class IBapi(EWrapper, EClient):
     def __init__(self):
         EClient.__init__(self, self) 

app = IBapi()
app.connect('127.0.0.1', 7497, 123)
app.run()

# Uncomment this section if unable to connect
# and to prevent errors on a reconnect
import time
time.sleep(2)
app.disconnect()
'''

# Retrieve the current ask price of Apple Stock (AAPL)
from datetime import datetime
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

import threading
import time


class IBapi(EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)
	def tickPrice(self, reqId, tickType, price, attrib):
		if tickType == 2 and reqId == 1:
			print('The current ask price is: ', price)

def run_loop():
	app.run()

app = IBapi()
app.connect('127.0.0.1', 7497, 123)

#Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1) #Sleep interval to allow time for connection to server

#Create contract object
apple_contract = Contract()
apple_contract.symbol = 'NFLX'
apple_contract.secType = 'STK'
apple_contract.exchange = 'SMART'
apple_contract.currency = 'USD'
'''
meta_contract = Contract()
meta_contract.symbol = 'NFLX'
meta_contract.secType = 'STK'
meta_contract.exchange = 'SMART'
meta_contract.currency = 'USD'
'''

queryTime = datetime.time.ToUniversalTime().AddMonths(-6).ToString("yyyyMMdd-HH:mm:ss");
EClient.reqHistoricalData(4003, apple_contract.USStockAtSmart(), queryTime, "1 M", "1 day", "SCHEDULE", 1, 1, False, None);

#Request Market Data
app.reqMktData(1, apple_contract, '', False, False, [])
#app.reqMktData(1, meta_contract, '', False, False, [])

time.sleep(10) #Sleep interval to allow time for incoming price data
app.disconnect()