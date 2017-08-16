from multiprocessing import Pool
import time


def myTask(n):
  time.sleep(n/2)
  return n*2

def myCallback(result):
  print("hi")
  print(result)

def main():
  print("apply_async")
  with Pool(4) as p:
    task1 = p.apply_async(func=myTask, args=(4,))
    task2 = p.apply_async(func=myTask, args=(3,))
    task3 = p.apply_async(func=myTask, args=(2,))
    task4 = p.apply_async(func=myTask, args=(1,))

    print(task1.get())
    print(task2.get())
    print(task3.get())
    print(task4.get())]

if __name__ == '__main__':
  main()
