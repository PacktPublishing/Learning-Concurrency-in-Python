import time
import random
import threading

def calculatePrimeFactors(n):
  primfac = []
  d = 2
  while d*d <= n:
    while (n % d) == 0:
      primfac.append(d)  
      n //= d
    d += 1
  if n > 1:
    primfac.append(n)
  return primfac

def executeProc():
  for i in range(1000):
    rand = random.randint(20000, 100000000)
    print(calculatePrimeFactors(rand))

def main():
  print("Starting number crunching")
  t0 = time.time()
  
  threads = []

  for i in range(10):
    thread = threading.Thread(target=executeProc)
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

  t1 = time.time()
  totalTime = t1 - t0
  print("Execution Time: {}".format(totalTime))


if __name__ == '__main__':
  main()