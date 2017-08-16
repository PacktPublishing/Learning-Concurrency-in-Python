import logging
from multiprocessing import Pool

logging.basicConfig(filename='myapp.log', level=logging.INFO,
  format='%(processName)-10s %(asctime)%s %(levelname)s %(message)s')

def myTask(n):
  logging.info("{} being processed".format(n))
  logging.info("Final Result: {}".format(n*2))
  return n*2

def main():
  with Pool(4) as p:
    p.map(myTask, [2,3,4,5,6,])

if __name__ == '__main__':
  main()