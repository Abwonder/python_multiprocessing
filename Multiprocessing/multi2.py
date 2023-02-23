import multiprocessing
import time  # to check time it takes

## define funtion
def counter1(num):
    cnt = 0
    for _ in range(num):
        cnt+=1
    print("counter1 done!")

def counter2(num):
    cnt = 0
    for _ in range(0, num, 2):
        cnt+=2
    print("counter2 done!")

if __name__ == "__main__":  ## do this for window users, linux no need to!
    ## all code comes inside the block!!
    N = 2 * 10 ** 8

    # single processing
    st = time.time() ## record start time!!!
    counter1(N)
    counter2(N)
    en = time.time() ## record end time!!!
    print("time taken: ", en-st)

    #multiprocessing
    st = time.time()
    p1 = multiprocessing.Process(target=counter1, args=(N,)) ## args must be passed as tuple
    p2 = multiprocessing.Process(target=counter2, args=(N,)) ## args must be passed as tuple

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    en = time.time()
    print("time taken= ", en-st)













