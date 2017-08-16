import threading
import time

def standardThread():
    print("Starting my Standard Thread")
    time.sleep(20)
    print("Ending my standard thread")

def daemonThread():
    while True:
      print("Sending Out Heartbeat Signal")
      time.sleep(2)

if __name__ == '__main__':
	standardThread = threading.Thread(target=standardThread)
	daemonThread = threading.Thread(target=daemonThread)
	daemonThread.setDaemon(True)
	daemonThread.start()
  
	standardThread.start()


