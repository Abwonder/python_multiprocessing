## Advancing the code into processes
## parallel multiprocessing!!!!
# added module
import multiprocessing
import time


start = time.perf_counter()  ## handles time counting

      ## created this in another file, and import
def do_something():
    print('Sleeping 1 second.....')
    time.sleep(1)
    print('Done Sleeping....')

if __name__=="__main__":  ## without this on linux it will work, but need to do this for windows
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target = do_something)
        p.start()  ## we cant apply join below because it will apply to each join
        ## and it will defeat the purpose of parallel programming
        ## we save it all and use join to iterate over all the started processes
        processes.append(p)
    # print(processes)

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round (finish-start, 2)} seconds(s)')

## proceed to mult4 to see those with arguements!!!!

