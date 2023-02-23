## parallel multiprocessing!!!!

import time
start = time.perf_counter()  ## handles time counting


def do_something():
    print('Sleeping 1 second.....')
    time.sleep(1)
    print('Done Sleeping....')

do_something()   ## each take 1 seconds so both 2
do_something()  ## check by running the code below!!!!

finish = time.perf_counter()

print(f'Finished in {round (finish-start, 2)} seconds(s)')

