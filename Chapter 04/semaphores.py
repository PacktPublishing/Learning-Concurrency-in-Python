import threading
import time
import random

class TicketSeller(threading.Thread):
  ticketsSold = 0

  def __init__(self, semaphore):
    threading.Thread.__init__(self);
    self.sem = semaphore
    print("Ticket Seller Started Work")

  def run(self):
    global ticketsAvailable
    running = True
    while running:
      self.randomDelay()
      
      self.sem.acquire()
      if(ticketsAvailable <= 0):
        running = False
      else:
        self.ticketsSold = self.ticketsSold + 1
        ticketsAvailable = ticketsAvailable - 1
        print("{} Sold One ({} left)".format(self.getName(), ticketsAvailable))
      self.sem.release()
    print("Ticket Seller {} Sold {} tickets in total".format(self.getName(), self.ticketsSold))

  def randomDelay(self):
    time.sleep(random.randint(0,4)/4)


# our sempahore primitive
semaphore = threading.Semaphore()
# Our Ticket Allocation
ticketsAvailable = 200

# our array of sellers
sellers = []
for i in range(4):
  seller = TicketSeller(semaphore)
  seller.start()
  sellers.append(seller)

# joining all our sellers
for seller in sellers:
  seller.join()
