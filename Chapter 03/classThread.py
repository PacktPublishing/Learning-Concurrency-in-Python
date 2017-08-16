from threading import Thread

class myWorkerThread(Thread):

  def __init__(self):
    print("Hello world")
    Thread.__init__(self)
  
  def run(self):
    print("Thread is now running")

myThread = myWorkerThread()
print("Created my Thread Object")
myThread.start()
print("Started my thread")
myThread.join()
print("My Thread finished")