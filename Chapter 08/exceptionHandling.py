import multiprocessing
import os, sys
import traceback

class MyProcess(multiprocessing.Process):
  
  def __init__(self, pipein):
    super(MyProcess, self).__init__()
    self.pipein = pipein

  def run(self):
    try:
      raise Exception("This broke stuff")
    except:
      except_type, except_class, tb = sys.exc_info()

      self.pipein = os.fdopen(self.pipein, 'w')
      self.pipein.write(str(tb))
      self.pipein.close()

def main():
  pipeout, pipein = os.pipe()

  childProcess = MyProcess(pipein)
  childProcess.start()
  childProcess.join()

  os.close(pipein)
  pipeout = os.fdopen(pipeout)

  pipeContent = pipeout.read()
  print("Exception: {}".format(pipeContent))

if __name__ == '__main__':
  main()
