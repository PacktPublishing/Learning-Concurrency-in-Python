from rx import Observable

list1 = [23, 38, 43, 23]

letters = Observable.from_(list1).to_blocking()
intervals = Observable.interval(1000)

def main():
  Observable \
    .zip(letters, intervals, lambda x, y: (x*y, y)) \
    .subscribe(lambda t: print(t))

if __name__ == '__main__':
  main()
  input("Press any key to quit\n")