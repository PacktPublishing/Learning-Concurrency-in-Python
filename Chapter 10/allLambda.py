from rx import Observable

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


source = Observable.create(buy_stock_events)

source.subscribe(on_next=lambda value: print("Received Instruction to buy {0}".format(value)),
                on_completed=lambda: print("Completed trades"),
                on_error=lambda e: print(e))