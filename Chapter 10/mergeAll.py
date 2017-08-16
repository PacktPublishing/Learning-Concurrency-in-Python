from rx import Observable

list1 = [23, 38, 43, 23]
list2 = [1,2,3,4]
source1 = Observable.from_(list1)
source2 = Observable.from_(list2)
sources = [source1, source2]

def main():
  Observable.from_(sources) \
    .merge_all() \
    .subscribe(lambda x: print(x))
  
  

if __name__ == '__main__':
  main()
  input("Press any key to quit\n")