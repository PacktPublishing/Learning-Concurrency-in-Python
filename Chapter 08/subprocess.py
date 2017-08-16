import multiprocessing

def myProcess():
  print("Currently Executing Child Process")
  print("This process has it's own instance of the GIL")

print("Executing Main Process")
print("Creating Child Process")
myProcess = multiprocessing.Process(target=myProcess)
myProcess.start()
myProcess.join()
print("Child Process has terminated, terminating main process")