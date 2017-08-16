import time
import random
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

values = [2,3,4,5,6,7,8]

def multiplyByTwo(n):
  time.sleep(random.randint(1,2))
  return 2 * n

def done(n):
  print("Done: {}".format(n))

def main():
  with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(multiplyByTwo, values)

    for result in results:
      done(result)

if __name__ == '__main__':
  main()