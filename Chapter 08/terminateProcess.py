import multiprocessing
import time

def daemonProcess():
  current_process = multiprocessing.current_process() 
  print("Child Process PID: {}".format(current_process.pid))
  time.sleep(20)

current_process = multiprocessing.current_process()
print("Main process PID: {}".format(current_process.pid))

myProcess = multiprocessing.Process(target=daemonProcess)
myProcess.start()
print("My Process has terminated, terminating main thread")

print("Terminating Child Process")
myProcess.terminate()

print("Child Process Successfully terminated")