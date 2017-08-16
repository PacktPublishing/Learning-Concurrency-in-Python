from multiprocessing import Pool
import timeit
import math

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
  with Pool(4) as p:
    print(p.map(is_prime, PRIMES))
  print("{} Seconds needed for multiprocessing pool".format(timeit.default_timer() - t1))

if __name__ == '__main__':
  main()