import threading
import queue
import random
import time

def mySubscriber(queue):
  while not queue.empty():
    item = queue.get()
    if item is None:
      break
    print("{} removed {} from the queue".format(threading.current_thread(), item))
    queue.task_done()
    time.sleep(1)

myQueue = queue.Queue()
for i in range(10):
  myQueue.put(i)

print("Queue Populated")

threads = []
for i in range(4):
  thread = threading.Thread(target=mySubscriber, args=(myQueue,))
  thread.start()
  threads.append(thread)

for thread in threads:
  thread.join()

