import gevent
from gevent import Greenlet

class MyNoopGreenlet(Greenlet):

  def __init__(self, seconds):
    Greenlet.__init__(self)
    self.seconds = seconds

  def _run(self):
    print("My Greenlet executing")
    gevent.sleep(self.seconds)

  def __str__(self):
    return 'MyNoopGreenlet(%s)' % self.seconds

g = MyNoopGreenlet(4)
g.start()
g.join()
print(g.dead)