import threading
import csv
import time

class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0

    def enqueue(self, val):
        self.queue.append(val)
        self.front += 1
    '''
    def dequeue(self):
        if self.rear < self.front:
            val = self.queue[self.rear]
            self.rear += 1
            return val
        else:
            return None
    '''
    def is_empty(self):
        return self.rear == self.front

    def clear(self):
        self.queue = []
        self.front = 0
        self.rear = 0
    
    def __iter__(self):
        self.current = self.rear
        return self

    def __next__(self):
        if self.current < self.front:
            val = self.queue[self.current]
            self.current += 1
            return val
        else:
            raise StopIteration
    

queue = Queue()
condition = threading.Condition()
loop_count = 0
valueset = False

class Product:
    def __init__(self, pid, pname, price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = float(price)
        self.quantity = int(quantity)
        self.total_price = self.price * self.quantity
        self.timestamp = time.strftime("%d_%b_%Y_%H_%M_%S")

def Producer(condition):
    global queue
    global loop_count
    global valueset

    with open("productslist.csv", "r", newline="") as fp:
        reader = csv.reader(fp)

        while True:
            with condition:
                queue.clear()
                loop_count += 1
                count = 0
                while count < 5:
                    try:
                        row = next(reader)
                        product = Product(row[0], row[1], row[2], row[3])
                        queue.enqueue(product)
                        count += 1
                    except StopIteration:
                        break

                if count == 0:
                    valueset = True
                    condition.notify()
                    break

                print(f"Produced {count} products for loop {loop_count}, waiting for consumption.")
                condition.notify()
                condition.wait()


def Consumer(condition):
    global queue
    global loop_count
    global valueset

    while True:
        with condition:
            if queue.is_empty() and not valueset:
                condition.wait()

            if not queue.is_empty():
                datetime = time.strftime("%d_%b_%Y_%H_%M_%S")
                filename = f"loop{loop_count}_{datetime}.csv"
                with open(filename, "w", newline="") as fp:
                    writer = csv.writer(fp)
                    for product in queue:
                        writer.writerow([
                            product.pid,
                            product.pname,
                            product.price,
                            product.quantity,
                            product.total_price,
                            product.timestamp
                        ])
                print(f"Consumed and wrote file: {filename}")
                queue.clear()
                condition.notify()
            elif valueset:
                break

producer_thread = threading.Thread(target=Producer, args=(condition,))
consumer_thread = threading.Thread(target=Consumer, args=(condition,))

consumer_thread.start()
producer_thread.start()

producer_thread.join()
consumer_thread.join()

print("All products finished.")