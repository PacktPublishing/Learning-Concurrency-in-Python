from rx import Observable, Observer
from random import randint

class Subscriber(Observer):

  def __init__(self, ident):
    self.id = ident

  def on_next(self, value):
    print("Subscriber: {} Received: {}".format(self.id, value))

  def on_completed(self):
    print("Subscriber: {} Received Events".format(self.id))

  def on_error(self, error):
    print("Error Occurred: {}".format(error))

three_emissions = Observable.range(1,3)
three_random_ints = three_emissions.map(lambda i: randint(1, 10000)).publish()

three_random_ints.subscribe(Subscriber("Grant"))
three_random_ints.subscribe(Subscriber("Barry"))
three_random_ints.subscribe(Subscriber("Sophie"))
three_random_ints.connect()