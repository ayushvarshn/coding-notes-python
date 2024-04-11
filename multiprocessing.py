# Each process runs independently and has its own memory space.
# multiprocessing module provides Array and Value objects to share data between processes.

import multiprocessing

class Account:
    def __init__(self):
        self.balance = multiprocessing.Value('i', 0)

    def withdraw(self,amt):
        for _ in range(amt):
            self.balance.value = self.balance.value - 1
        

    def deposit(self, amt):
        for _ in range(amt):
            self.balance.value = self.balance.value + 1  


    def perform_transaction(self):
        p1 = multiprocessing.Process(target=self.withdraw, args=(1000,))
        p2 = multiprocessing.Process(target=self.deposit, args=(10000,))

        p1.start()
        p2.start()

        p1.join()
        p2.join()
        print(self.balance.value)

if __name__ == "__main__":
    acc =  Account()
    acc.perform_transaction()
