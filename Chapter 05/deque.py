import collections

doubleEndedQueue = collections.deque('123456')

print("Dequeue: {}".format(doubleEndedQueue))

for item in doubleEndedQueue:
  print("Item {}".format(item))

print("Left Most Element: {}".format(doubleEndedQueue[0]))
print("Right Most Element: {}".format(doubleEndedQueue[-1]))

doubleEndedQueue.remove('1')
print("Removing Element: {}".format(doubleEndedQueue))