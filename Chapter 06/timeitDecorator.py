import random
import timeit
import time
 
def timethis(func):

    def function_timer(*args, **kwargs):
        start_time = timeit.default_timer()
        value = func(*args, **kwargs)
        runtime = timeit.default_timer() - start_time
        print("Function {} took {} seconds to run".format(func.__name__, runtime))
        return value
    return function_timer
 
@timethis
def long_runner():
    for x in range(3):
        sleep_time = random.choice(range(1,3))
        time.sleep(sleep_time)
 
if __name__ == '__main__':
    long_runner()