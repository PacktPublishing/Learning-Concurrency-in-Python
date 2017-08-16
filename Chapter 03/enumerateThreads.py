import threading
import time
import random

def myThread(i):
  print("Thread {}: started".format(i))
  time.sleep(random.randint(1,5))
  print("Thread {}: finished".format(i))


def main():
  for i in range(4):
    thread = threading.Thread(target=myThread, args=(i,))
    thread.start()

  print("Enumerating: {}".format(threading.enumerate()))

if __name__ == '__main__':
  main()