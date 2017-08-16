from multiprocessing import Pool
import time
import os

def myTask(x, y):
  print("{} Executed my task".format(os.getpid()))
  return y*2

def main():
  with Pool(processes=1, maxtasksperchild=2) as p:
     print(p.starmap_async(myTask, [(4,3),(2,1), (3,2), (5,1)]).get())
     print(p.starmap_async(myTask, [(4,3),(2,1), (3,2), (2,3)]).get())

if __name__ == '__main__':
  main()
