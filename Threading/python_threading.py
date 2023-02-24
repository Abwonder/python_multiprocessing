import time
start = time.perf_counter()

def do_something():
    print('Sleeping 1 second.......')
    time.sleep(1)
    print('Done Sleeping .......')

do_something()   ### this implies each waits 1seconds, so total should give amount of seconds
do_something()
do_something()
do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')

## Chech the next code to see the improvement to adding threading######