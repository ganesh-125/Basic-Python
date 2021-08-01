from multiprocessing import Pool
import time

def  mysquare(a):
    return (a*a)

if __name__ == '__main__':
    start = time.perf_counter()
    pool = Pool()
    array = range(100)
    result = pool.map(mysquare,array)
    print(result)
    end = time.perf_counter()
    print(f'Finished in {round(end-start,2)} Seconds')
    