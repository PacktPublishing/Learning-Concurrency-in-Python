import multiprocessing
import time

def myProcess():
  current_process = multiprocessing.current_process().pid 
  print("Child Process PID: {}".format(current_process.pid))
  time.sleep(20)

current_process = multiprocessing.current_process()
print("Main process PID: {}".format(current_process.pid))

myProcess = multiprocessing.Process(target=myProcess)
myProcess.start()
print("My Process has terminated, terminating main thread")