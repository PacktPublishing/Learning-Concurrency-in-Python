import asyncio
import logging
import time

logging.basicConfig(level=logging.DEBUG)

async def myWorker():
  logging.info("My Worker Coroutine Hit")
  time.sleep(1)

async def main():
  logging.debug("My Main Function Hit")
  await asyncio.wait([myWorker()])

loop = asyncio.get_event_loop()
loop.set_debug(True)
try:
  loop.run_until_complete(main())
finally:
  loop.close()