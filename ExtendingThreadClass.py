from threading import Thread
import time

class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(5):
            print(f"{self.name} is running iteration {i}")
            time.sleep(1)

        print(f"{self.name} has completed it's work.")
        #print(f"Thread {self.name} is starting.")
        #time.sleep(2)
        #print(f"Thread {self.name} is finishing.")

t1 = MyThread("Thread-1")
t2 = MyThread("Thread-2")

t1.start()
t2.start()

t1.join()
t2.join()

print("Main Thread is completed.") 