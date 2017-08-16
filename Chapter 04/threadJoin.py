import threading
import time

def ourThread(i):
  print("Thread {} Started".format(i))
  time.sleep(i*2)
  print("Thread {} Finished".format(i))

def main():
  thread = threading.Thread(target=ourThread, args=(1,))
  thread.start()

  print("Is thread 1 Finished?")

  thread2 = threading.Thread(target=ourThread, args=(2,))
  thread2.start()
  thread2.join()

  print("Thread 2 definitely finished")

if __name__ == '__main__':
  main()