import threading
import time

count = 0
valueset = False

def Producer(condition):
    global count
    global valueset
    
    with condition:
        while count < 10:
            if not valueset:
                count = count + 1
                valueset = True
                print(f"Producer: {count}")
                condition.notify()
            else:
                print("Already produced, waiting for consumption.")
                condition.wait()

def Counsumer(condition):
    global count
    global valueset
    with condition:
        while count < 10:
            if not valueset:
                print("Waiting for production")
                condition.wait()
            else:
                print(f"Consumed: {count}")
                valueset = False
                condition.notify()
        

condition = threading.Condition()

consumer_thread = threading.Thread(target=Counsumer, args=(condition,))
producer_thread = threading.Thread(target=Producer, args=(condition,))

consumer_thread.start()
producer_thread.start()

consumer_thread.join()
producer_thread.join()

print("Threads have finished execution.")

'''
    I want a queue. you have to take a queue. you need to write a producer and a consumer. Producer will take some product class objects from the csv file, (read line by line 5 lines each time)(5 products)and put them in the queue. So everytime producer will create some product class objects( 5 objetcs). and put them into the queue. Once done, producer will give instruction to consumer and then consumer will consume these product objects from the queue
    and calculate the total price based on the quantity and store that in a csv file.
    csv file should be created with loop number (loop1, loop2, loop3 ..) and date and time. (datetime) use (import time)
    once this is done again producer will produce another 5 product objetcs and that will be continued. 

    i.e from csv -> ( it contains 25 product objects ) producer will read 5 products at a time and notify consumer, consumer will calculate total price of each product and create a new file each time for set of 5 products and stores the products.


    in csv:
    pid, pname, price, quantity.

    what consumer should generate:
    pid, pname, price, quantity, total_price, datetime
'''