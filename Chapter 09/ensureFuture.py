import asyncio
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor

def myTask():
  print("Hello World")

myFuture = Future()
myWrappedFuture = asyncio.wrap_future(myFuture)

with ThreadPoolExecutor(max_workers=4) as executor:
    future = executor.submit(task, (4))
    myWrappedFuture = asyncio.wrap_future(future)

loop = asyncio.get_event_loop()
try:
  loop.run_until_complete(myWrappedFuture())
finally:
  loop.close()