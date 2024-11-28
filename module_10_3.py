import threading
import random
import time

class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, activity=100):
        for i in range(activity):
            replenishment_of_funds = random.randint(50, 500)
            self.balance += replenishment_of_funds
            print(f'Пополнение: {replenishment_of_funds}. Баланс: {self.balance}')
            time.sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self, activity=100):
        for i in range(activity):
            withdrawal_of_funds = random.randint(50, 500)
            print(f'Запрос на {withdrawal_of_funds}')
            if withdrawal_of_funds <= self.balance:
                self.balance -= withdrawal_of_funds
                print(f'Снятие: {withdrawal_of_funds}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()


bk = Bank(1000)

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
