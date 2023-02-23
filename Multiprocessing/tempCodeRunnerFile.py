## Import all the module needed

import math
import multiprocessing
import time

def check_prime(N):
    arr = [True]*N
    for num in range(N):
        if num<2:
            arr[num]=False
        elif num>2:
            for j in range(2, math.ceil(math.sqrt(num))+1):
                arr[num] = False
                break
    return arr

import math
def check_prime_multi(num):
    if num<2:
        return num, False
    elif num==2:
        return num, True
    else:
        for j in range(2, math.ceil(math.sqrt(num))+1):
            if num%j==0:
                # print("It worked!!!")
                # print("else workded: %d" %num)
                return num, False
    return num, True

# # print(check_prime_multi(50))
# return_num = check_prime_multi(50) / 5
# print(return_num)


if __name__=="__main__":
    ##single processing
    N = 2 * 10**6
    st = time.time()
    results  = check_prime(N)
    print(results[:30])
    en=time.time()
    print("time taken= ", en-st)


    #multiprocessing
    st = time.time()
    num_arr = range(N)
    num_process = 10  ## tells the multiprocess number of operation to carryout parallel (i.e same time)
    with multiprocessing.Pool(processes=num_process) as pool: ## use here!!, at pool rep the multiprocess object
        results=pool.map(check_prime_multi, num_arr)  ## mapped the function check_prime_multi on num_arr
    pool.close()   ## alway close the process applicable to file handling and threading
    en = time.time()
    print(results[:30])
    print("Time taken: ", en-st)



# I understand this now!!!!
# import math
# abioye = [True]*30
# print(abioye)
