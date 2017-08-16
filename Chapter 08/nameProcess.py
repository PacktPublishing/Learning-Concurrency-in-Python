import multiprocessing

def myProcess():
  print("{} Just performed X".format(multiprocessing.current_process().name))

def main():
  childProcess = multiprocessing.Process(target=myProcess, name='My-Awesome-Process')
  childProcess.start()
  childProcess.join()

if __name__ == '__main__':
  main()