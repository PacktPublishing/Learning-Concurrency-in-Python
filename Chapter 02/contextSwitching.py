import threading
import time

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

def main():
  t0 = time.time()
  for i in range(35):
    F(i)
  t1 = time.time()
  print("Total Execution Time {}".format(t1-t0))

if __name__ == '__main__':
  main()