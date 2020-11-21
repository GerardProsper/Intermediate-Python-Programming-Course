
from multiprocessing import Process, Value, Array, Lock
import os
import time

#Lock prevents another process from accessing different process at the same time


def square_numbers():
    for i in range(1000):
        i * i


# if __name__ == "__main__":
#     processes = []
#     num_processes = os.cpu_count()
#     # number of CPUs on the machine. Usually a good choice for the number of processes
#
#     #create processes and assign a function for each proces
#     for i in range(num_processes):
#         process = Process(target=square_numbers)
#         processes.append(process)
#
#     #start
#     for process in processes:
#         process.start()
#
#     # wait for all processes to finish
#     # block the main program until these processes are finished
#     for process in processes:
#         process.join()
#
# print('end main') #only reach this point when all process are done




def add_100(numbers,lock):
    for i in range(100):
        time.sleep(0.01)
        # lock.acquire()
        # number.value += 1
        # lock.release() # must use this if have lock.acquire
        #with lock:
        #    number.value += 1
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1

if __name__ == "__main__":
    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('array at the beginning is', shared_array[:])
    # shared_number = Value('i', 0)
    # print('Number at beginning is', shared_number.value)


    p1 = Process(target=add_100, args=(shared_array,lock)) #this is tuple
    p2 = Process(target=add_100, args=(shared_array,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('array at the end is', shared_array[:])
    # print('Number at end is',shared_number.value)

#stopped at 4:43:44 in multiprocessing