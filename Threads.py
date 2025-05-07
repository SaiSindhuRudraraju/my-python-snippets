'''
    when we run a program, the operating system creates a process, in the process a thread will be created and our program will execute in that thread.
    process-> main-thread -> main()
    One thread can do one task. If we want to perform multiple tasks, instead of creating multiple processes, we create multiple threads.
'''

import threading
import time
'''
class Calculate:
    def sum(x,y):
        print(__name__)
        print(threading.current_thread().name)
        return x+y

Calculate.sum(1,2)
Calculate.sum(3,4)

print(__name__)
print(threading.current_thread().name)
'''

def print_numbers():
    for i in range(5):
        print(f"{threading.current_thread().name} - {i}")
        time.sleep(1)

t1 = threading.Thread(target=print_numbers, name="Thread-1")
t1.start()

t2 = threading.Thread(target=print_numbers, name="Thread-2")
t2.start()

t1.join()
t2.join()

#main thread
for i in range(5,-1,-1):
    print(f"{threading.current_thread().name} - {i}")
    #time.sleep(1)