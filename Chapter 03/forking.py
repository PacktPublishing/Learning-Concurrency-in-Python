import os 

def child(): 
  print("We are in the child process with PID= %d"%os.getpid()) 
  
def parent(): 
  print("We are in the parent process with PID= %d"%os.getpid())
  newRef=os.fork() 
  if newRef==0: 
    child() 
  else: 
    print("We are in the parent process and our child process has PID= %d"%newRef)
    
parent()