import threading
import time

def myChildThread():
  print("Child Thread Starting")
  time.sleep(5)
  print("Current Thread ----------")
  print(threading.current_thread())
  print("-------------------------")
  print("Main Thread -------------")
  print(threading.main_thread())
  print("-------------------------")
  print("Child Thread Ending")


child = threading.Thread(target=myChildThread)
child.start()
child.join()
