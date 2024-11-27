import threading
import time
class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power


    def run(self, sum_enemy=100, counter_days=0):
        print(f'{self.name}, на нас напали!')
        while sum_enemy:
            sum_enemy -= self.power
            time.sleep(1)
            counter_days += 1
            print(f'{self.name} сражается {counter_days} дней, осталось {sum_enemy} воинов')
        print(f'{self.name} одержал победу спустя {counter_days} дней(дня)!')



# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились')
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения
