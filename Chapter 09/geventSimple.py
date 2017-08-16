import gevent
from gevent import socket

def main():
  urls = ['www.google.com', 'www.example.com', 'www.python.org']
  jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
  gevent.joinall(jobs, timeout=2)
  print([job.value for job in jobs])

if __name__ == '__main__':
  main()