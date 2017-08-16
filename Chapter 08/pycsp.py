from pycsp.parallel import *
import time

@process
def Process1():
  time.sleep(1)  # Sleep 1 second
  print('process1 exiting')
 
@process
def Process2():
  time.sleep(2)  # Sleep 2 seconds
  print('process2 exiting')
 
Parallel(Process1(), Process2())  # Blocks
print('program terminating')