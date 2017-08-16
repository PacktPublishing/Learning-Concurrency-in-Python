from functional import seq
from collections import namedtuple

Stock = namedtuple('Stock', 'tckr price')
stocks = [
  Stock('AMZN', 100), 
  Stock('FACE', 200), 
  Stock('JPM', 80), 
  Stock('TSLA', 500), 
  Stock('TSLA', 450) 
]

costs = seq(stocks)\
  .filter(lambda x: x.tckr == 'TSLA')\
  .map(lambda x: x.price)\
  .sum()

print("Total cost of TSLA transactions: {}".format(costs))
