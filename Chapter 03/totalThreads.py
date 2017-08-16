import threading
import time
import random

def myThread(i):
  print("Thread {}: started".format(i))
  time.sleep(random.randint(1,5))
  print("Thread {}: finished".format(i))


def main():
  for i in range(random.randint(2,50)):
    thread = threading.Thread(target=myThread, args=(i,))
    thread.start()

  time.sleep(4)
  print("Total Number of Active Threads: {}".format(threading.active_count()))

if __name__ == '__main__':
  main()