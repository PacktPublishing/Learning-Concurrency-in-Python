import threading
import time
import random

def executeThread(i):
  print("Thread {} started".format(i))
  sleepTime = random.randint(1,10)
  time.sleep(sleepTime)
  print("Thread {} finished executing".format(i))

for i in range(10):
  thread = threading.Thread(target=executeThread, args=(i,))
  thread.start()

  print("Active Threads:" , threading.enumerate())