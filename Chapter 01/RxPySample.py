import rx
from rx import Observable, Observer

# Here we define our custom observer which
# contains an on_next method, an on_error method
# and an on_completed method
class temperatureObserver(Observer):

  # Every time we receive a temperature reading
  # this method is called
  def on_next(self, x):
    print("Temperature is: %s degrees centigrade" % x)
    if (x > 6):
      print("Warning: Temperate Is Exceeding Recommended Limit")
    if (x == 9):
      print("DataCenter is shutting down. Temperature is too high")

  # if we were to receive an error message
  # we would handle it here
  def on_error(self, e):
    print("Error: %s" % e)
  
  # This is called when the stream is finished
  def on_completed(self):
    print("All Temps Read")

# Publish some fake temperature readings 
xs = Observable.from_iterable(range(10))
# subscribe to these temperature readings
d = xs.subscribe(temperatureObserver())