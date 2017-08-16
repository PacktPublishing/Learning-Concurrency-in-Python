import asyncio

async def myFuture(future):
  await asyncio.sleep(1)
  future.set_result("My Future Has Completed")

async def main():
  future = asyncio.Future()
  await asyncio.ensure_future(myFuture(future))
  print(future.result())

loop = asyncio.get_event_loop()
try:
  loop.run_until_complete(main())
finally:
  loop.close()