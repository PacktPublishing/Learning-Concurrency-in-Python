from multiprocessing import Process
import time

def myWorker():
  t1 = time.time()
  print("Process started at: {}".format(t1))
  time.sleep(20)

myProcess = Process(target=myWorker)
print("Process {}".format(myProcess))
myProcess.start()
print("Terminating Process...")
myProcess.terminate()
myProcess.join()
print("Process Terminated: {}".format(myProcess))

