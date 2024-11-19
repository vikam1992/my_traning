# lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'
lmb_func = list(map(lambda x, y: x == y,first, second))
print(lmb_func)

# Замыкание:
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open('example.txt', 'a', encoding='utf-8') as file:
            for string in data_set:
                file.write(str(string) + '\n')
              
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:
from random import choice
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
