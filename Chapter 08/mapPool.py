from multiprocessing import Pool
import time

def myTask(n):
  time.sleep(n+2)
  return n+2

def main():
  with Pool(4) as p:
     for iter in p.imap_unordered(myTask, [1,3,2,1]):
       print(iter)
     

if __name__ == '__main__':
  main()
