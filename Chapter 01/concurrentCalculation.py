import time
import random
from multiprocessing import Process

# This does all of our prime factorization on a given number 'n'
def calculatePrimeFactors(n):
  primfac = []
  d = 2
  while d*d <= n:
    while (n % d) == 0:
      primfac.append(d)  # supposing you want multiple factors repeated
      n //= d
    d += 1
  if n > 1:
    primfac.append(n)
  return primfac

# We split our workload from one batch of 10,000 calculations
# into 10 batches of 1,000 calculations
def executeProc():
  for i in range(1000):
    rand = random.randint(20000, 100000000)
    print(calculatePrimeFactors(rand))

def main():
  print("Starting number crunching")
  t0 = time.time()
  
  procs = []

  # Here we create our processes and kick them off
  for i in range(10):
    proc = Process(target=executeProc, args=())
    procs.append(proc)
    proc.start()

  # Again we use the .join() method in order to wait for 
  # execution to finish for all of our processes
  for proc in procs:
    proc.join()

  t1 = time.time()
  totalTime = t1 - t0
  # we print out the total execution time for our 10
  # procs.
  print("Execution Time: {}".format(totalTime))


if __name__ == '__main__':
  main()