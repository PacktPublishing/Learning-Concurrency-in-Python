from multiprocessing import Pool
import time
import os

def myTask(n):
  print("Task processed by Process {}".format(os.getpid()))
  return n*2

def main():
  print("apply_async")
  with Pool(4) as p:
    tasks = []

    for i in range(4):
      task = p.apply_async(func=myTask, args=(i,))
      tasks.append(task)

    for task in tasks:
      task.wait()
      print("Result: {}".format(task.get()))
  
    

if __name__ == '__main__':
  main()
