# timeitTest.py
import threading
import random
import time

def myWorker():
  for i in range(5):
    print("Starting wait time")
    time.sleep(random.randint(1,5))
    print("Completed Wait")

thread1 = threading.Thread(target=myWorker)
thread2 = threading.Thread(target=myWorker)
thread3 = threading.Thread(target=myWorker)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()