## add argument

## Advancing the code into processes
## parallel multiprocessing!!!!
# added module

# import multiprocessing   ## No need for this!!!
import concurrent.futures
import time


start = time.perf_counter()  ## handles time counting

      ## created this in another file, and import
def do_something(seconds):
    print(f'Sleeping {seconds} second(s).....')
    time.sleep(seconds)
    return f'Done Sleeping for {seconds}....'   ## return instead of print
    # print('Done Sleeping....')

if __name__=="__main__":  ## without this on linux it will work, but need to do this for windows
    ## adding varying secs

    secs = [5,4,3,2,1]
    
    ## create the executor for the new module in use___ concurrent.future
    with concurrent.futures.ProcessPoolExecutor() as executor:
        ## using map function from math
        results = executor.map(do_something, secs)  ## it handles the joining wen the processes are done!!
        ## because this does not return future rather the actual result of object, then we can print out with nothing more to add
        
        for result in results:
            print(result)

        
        
        
        # Using list comprehension
        # results = [executor.submit(do_something, sec) for sec in secs]

        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

       
       
       
        # ## this schedules a function to be executed and submit a future object!!!, also helps us to check if a function is running or completed using the result
        # f1 = executor.submit(do_something, 1)  ## process 1 function at a time
        # print(f1.result())  ## made possible bcos of return used in the function
    
    ######## Below commented codes are not needed since we are using concurrent.future not multiprocessing module/library
    
    # processes = []
    # for _ in range(10):
    #     # p = multiprocessing.Process(target = do_something, args=[1.5]) # the args will fill up the seconds with its value at every for loop!!
    #     p = multiprocessing.Process(target = do_something, args=(1.5,))  # I used tuple format for args and its still works any can be used!!
    #     p.start()  ## we cant apply join below because it will apply to each join
    #     ## and it will defeat the purpose of parallel programming
    #     ## we save it all and use join to iterate over all the started processes
    #     processes.append(p)
    # # print(processes)

    # for process in processes:
    #     process.join()

    finish = time.perf_counter()

    print(f'Finished in {round (finish-start, 2)} seconds(s)')

# Note: this runs only one time, so to run multiple time we can use loop with the above or list comprehension

## proceed to see the best way to implement this in real project ==== mult5!!!!

