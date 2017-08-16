import time
import random
from concurrent.futures import ThreadPoolExecutor

def someTask(n):
  print("Executing Task {}".format(n))
  time.sleep(n)
  print("Task {} Finished Executing".format(n))

def main():
  with ThreadPoolExecutor(max_workers=2) as executor:
    task1 = executor.submit(someTask, (1))
    task2 = executor.submit(someTask, (2))
    print(executor.shutdown(wait=False))
    task3 = executor.submit(someTask, (3))
    task4 = executor.submit(someTask, (4))
  
if __name__ == '__main__':
  main()
