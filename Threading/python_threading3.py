import threading  ## threading module 

import time
start = time.perf_counter()

def do_something():
    print('Sleeping 1 second.......')
    time.sleep(1)
    print('Done Sleeping .......\n')

# do_something()   ### this implies each waits 1seconds, so total should give amount of seconds
# do_something()   
# do_something()
# do_something()   will change them all the thread below

## when running your code on windows do this if linux need to add if __name__ line

# if __name__=="__main":  ## this works without this!!!
# t1 = threading.Thread(target = do_something) ## pass it in without object!!!
# t2 = threading.Thread(target = do_something)
# t3 = threading.Thread(target = do_something)
# t4 = threading.Thread(target = do_something)

# ## start() method implements threading

# t1.start()  ## use the join method to wait until everything is done before it proceed to run other code
# t2.start()  ## there is possibility that when the codes are sleeping other lower line of code can be executed
# t3.start()
# t4.start()

# t1.join()
# t2.join()
# t3.join()
# t4.join()

# Now we will be running by loop instead of doing reiterating it one after the other
threadlist = []
for _ in range(40):
    t = threading.Thread(target = do_something)
    t.start()
    threadlist.append(t)

for thread in threadlist:
    thread.join()
     
finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')

## Chech the next code to see the improvement to adding threading######