import threading
import time

class myWorker():

  def __init__(self):
    self.a = 1
    self.b = 2
    self.rlock = threading.RLock()
  
  def modifyA(self):
    with self.rlock:
      print("Modifying A : RLock Acquired: {}".format(self.rlock._is_owned()))
      print("{}".format(self.rlock))
      self.a = self.a + 1
      time.sleep(5)

  def modifyB(self):
    with self.rlock:
      print("Modifying B : RLock Acquired: {}".format(self.rlock._is_owned()))
      print("{}".format(self.rlock))
      self.b = self.b - 1
      time.sleep(5)

  def modifyBoth(self):
    with self.rlock:
      print("Rlock acquired, modifying A and B")
      print("{}".format(self.rlock))
      self.modifyA()
      print("{}".format(self.rlock))
      self.modifyB()
    print("{}".format(self.rlock))


workerA = myWorker()
workerA.modifyBoth()
