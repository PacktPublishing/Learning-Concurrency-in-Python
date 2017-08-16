import time

def my_generator():
  for i in range(5):
    time.sleep(1)
    yield i

generator = my_generator()

for generated in generator:
  print(generated)