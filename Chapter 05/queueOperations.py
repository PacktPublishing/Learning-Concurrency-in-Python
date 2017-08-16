import threading
import queue
import random
import time

def mySubscriber(queue):
  while True:
    item = queue.get()
    if item is None:
      break
    print("{} removed {} from the queue".format(threading.current_thread(), item))
    print("Queue Size is now: {}".format(queue.qsize()))
    queue.task_done()

myQueue = queue.Queue()
for i in range(10):
  myQueue.put(i)

print("Queue Populated")

threads = []
for i in range(4):
  thread = threading.Thread(target=mySubscriber, args=(myQueue,))
  thread.start()
  threads.append(thread)

myQueue.join()

