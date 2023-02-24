import threading  ## threading module 

# passing argument into the threading 
import time
start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second.......')
    time.sleep(seconds)
    print('Done Sleeping .......\n')

# Now we will be running by loop instead of doing reiterating it one after the other
threadlist = []
for _ in range(40):
    t = threading.Thread(target = do_something, args=[1.5])  ## added args for 1.5
    t.start()
    threadlist.append(t)

for thread in threadlist:
    thread.join()
     
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')

### Lets move into the best way to run this!!!!