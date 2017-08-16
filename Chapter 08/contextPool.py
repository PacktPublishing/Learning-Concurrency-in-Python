from multiprocessing import Pool

def task(n):
    print(n)

def main():
    with Pool(4) as p:
        print(p.map(task, [2,3,4]))

if __name__ == '__main__':
    main()