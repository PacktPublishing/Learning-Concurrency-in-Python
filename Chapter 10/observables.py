from rx import Observable, Observer

stocks = [
  { 'TCKR' : 'APPL', 'PRICE': 200},
  { 'TCKR' : 'GOOG', 'PRICE': 90},
  { 'TCKR' : 'TSLA', 'PRICE': 120},
  { 'TCKR' : 'MSFT', 'PRICE': 150},
  { 'TCKR' : 'INTL', 'PRICE': 70},
]

def buy_stock_events(observer):
  for stock in stocks:
    if(stock['PRICE'] > 100):
      observer.on_next(stock['TCKR'])
  observer.on_completed()

class StockObserver(Observer):

  def on_next(self, value):
    print("Received Instruction to buy {0}".format(value))

  def on_completed(self):
    print("All Buy Instructions have been received")

  def on_error(self, error):
    print("Error Occurred: {0}".format(error))

source = Observable.create(buy_stock_events)
source.subscribe(StockObserver())