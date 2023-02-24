import concurrent.futures

# we dont need threading anymore
# import threading  ## threading module 

# passing argument into the threading 
import time
start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second.......')
    time.sleep(seconds)
    print('Done Sleeping .......\n')

with concurrent.futures.ThreadPoolExecutor() as executor:
    # use list comprehension
    secs = [5,4,3,2,1]
    results = [executor.submit(do_something, i) for i in secs]  # will run for the number of ranges and oupt list containg 10 results
    for f in results:
       print(f.result())
    
     
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')

### Lets move into the best way to run this!!!!