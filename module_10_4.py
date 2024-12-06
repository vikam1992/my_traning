import time
import random
from threading import Thread
from queue import Queue

# Класс Table (Стол)
class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None     # Гость за столом (по умолчанию None)

# Класс Guest (Гость), наследуется от Thread (поток)
class Guest(Thread):
    def __init__(self, name):
        super().__init__()  # Инициализация родительского класса Thread
        self.name = name    # Имя гостя

    def run(self):
        # Имитация процесса еды, случайная задержка от 3 до 10 секунд
        time_to_eat = random.randint(3, 10)
        time.sleep(time_to_eat)

# Класс Cafe (Кафе)
class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)  # Список столов в кафе
        self.queue = Queue()        # Очередь для гостей

    def guest_arrival(self, *guests):
        for guest in guests:
            # Поиск свободного стола
            free_table = next((table for table in self.tables if table.guest is None), None)
            if free_table:
                # Если есть свободный стол, сажаем гостя
                free_table.guest = guest
                guest.start()  # Запускаем поток гостя
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                # Если свободных столов нет, добавляем гостя в очередь
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    # Гость за столом закончил есть
                    print(f"{table.guest.name} покушал(-а) и ушёл(-ла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол

                    # Проверяем, есть ли гости в очереди
                    if not self.queue.empty():
                        next_guest = self.queue.get()  # Берём следующего гостя из очереди
                        table.guest = next_guest       # Сажаем за стол
                        next_guest.start()             # Запускаем поток нового гостя
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

            time.sleep(1)  # Задержка для имитации времени обслуживания

# Основной код
if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]

    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]

    # Создание гостей
    guests = [Guest(name) for name in guests_names]

    # Заполнение кафе столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)

    # Обслуживание гостей
    cafe.discuss_guests()
