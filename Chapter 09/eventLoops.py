import asyncio

def got_result(future):
    print(future.result())

@asyncio.coroutine
def slow_operation():
    yield from asyncio.sleep(1)
    return 'Future is done!'

def main():
  loop = asyncio.get_event_loop()
  task = loop.create_task(slow_operation())
  task.add_done_callback(got_result)
  loop.run_until_complete(task)

if __name__ == '__main__':
  main()