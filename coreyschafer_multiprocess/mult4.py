## add argument

## Advancing the code into processes
## parallel multiprocessing!!!!
# added module
import multiprocessing
import time


start = time.perf_counter()  ## handles time counting

      ## created this in another file, and import
def do_something(seconds):
    print(f'Sleeping {seconds} second(s).....')
    time.sleep(seconds)
    print('Done Sleeping....')

if __name__=="__main__":  ## without this on linux it will work, but need to do this for windows
    processes = []
    for _ in range(10):
        # p = multiprocessing.Process(target = do_something, args=[1.5]) # the args will fill up the seconds with its value at every for loop!!
        p = multiprocessing.Process(target = do_something, args=(1.5,))  # I used tuple format for args and its still works any can be used!!
        p.start()  ## we cant apply join below because it will apply to each join
        ## and it will defeat the purpose of parallel programming
        ## we save it all and use join to iterate over all the started processes
        processes.append(p)
    # print(processes)

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round (finish-start, 2)} seconds(s)')

## proceed to see the best way to implement this in real project ==== mult5!!!!

