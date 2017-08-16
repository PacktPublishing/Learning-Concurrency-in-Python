import multiprocessing as mp
import queue

def myProcess(ns):
  # Update values within our namespace
  print(ns.x)
  ns.x = 2

def main():
  manager = mp.Manager()
  ns = manager.Namespace()
  ns.x = 1

  print(ns)
  
  process = mp.Process(target=myProcess, args=(ns,))
  process.start()
  process.join()
  print(ns)

if __name__ == '__main__':
  main()