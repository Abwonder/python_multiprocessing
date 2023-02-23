## Advancing the code into processes
## parallel multiprocessing!!!!
# added module
import multiprocessing

import time
start = time.perf_counter()  ## handles time counting


def do_something():
    print('Sleeping 1 second.....')
    time.sleep(1)
    print('Done Sleeping....')

if __name__=="__main__":
    p1 = multiprocessing.Process(target = do_something)  
    p2 = multiprocessing.Process(target = do_something)  

    p1.start()   ## this initiates the process to work
    p2.start() ##

    # To ensure the processes finish before other things runs
    p1.join()
    p2.join()

    p1.close()
    p2.close()
    
    finish = time.perf_counter()

    print(f'Finished in {round (finish-start, 2)} seconds(s)')

