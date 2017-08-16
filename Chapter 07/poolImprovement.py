import timeit
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import math

values = [40000000, 30000000, 20000000, 10000000]

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    112272535095293,
    115280095190773,
    115797848077099,
    112272535095293,
    115280095190773,
    115797848077099,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True
    
def main():

  t1 = timeit.default_timer()
  with ProcessPoolExecutor(max_workers=4) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

  print("{} Seconds Needed for ProcessPoolExecutor".format(timeit.default_timer() - t1))
  
  t2 = timeit.default_timer()
  with ThreadPoolExecutor(max_workers=4) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
  print("{} Seconds Needed for ThreadPoolExecutor".format(timeit.default_timer() - t2))

  t3 = timeit.default_timer()
  for number in PRIMES:
    isPrime = is_prime(number)
    print("{} is prime: {}".format(number, isPrime))
  print("{} Seconds needed for single threaded execution".format(timeit.default_timer()-t3))

if __name__ == '__main__':
  main()