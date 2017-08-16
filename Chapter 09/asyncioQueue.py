import asyncio
import random
import time

@asyncio.coroutine
def newsProducer(myQueue):
  while True:
    yield from myQueue.put(random.randint(1,5))
    yield from asyncio.sleep(1)
    
@asyncio.coroutine
def newsConsumer(myQueue):
  while True:
    articleId = yield from myQueue.get()
    print("News Reader Consumed News Article {}", articleId)

myQueue = asyncio.Queue()

loop = asyncio.get_event_loop()

loop.create_task(newsProducer(myQueue))
loop.create_task(newsConsumer(myQueue))

try:
  loop.run_forever()
finally:
  loop.close()