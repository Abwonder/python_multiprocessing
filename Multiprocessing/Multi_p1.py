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

N = 2 * 10 ** 8

# single processing
st = time.time() ## record start time!!!
counter1(N)
counter2(N)
en = time.time() ## record end time!!!
print("time taken: ", en-st)
