import asyncio


# Асинхронная функция для участия силача в соревновании
async def start_strongman(name, power):
    """
    name: str - Имя силача.
    power: int - Сила силача, обратнопропорционально влияет на задержку между поднятиями шаров.
    """
    print(f'Силач {name} начал соревнования.')

    # Силач поднимает 5 шаров с задержкой, зависящей от силы
    for i in range(1, 6):  # Поднимаем 5 шаров
        await asyncio.sleep(1 / power)  # Задержка обратна силе
        print(f'Силач {name} поднял {i} шар.')

    print(f'Силач {name} закончил соревнования.')


# Асинхронная функция для запуска соревнований
async def start_tournament():
    """
    Организует соревнование между тремя силачами.
    """
    # Определяем участников соревнований
    participants = [
        ('Pasha', 3),  # Имя и сила первого участника
        ('Denis', 4),  # Имя и сила второго участника
        ('Apollon', 5)  # Имя и сила третьего участника
    ]

    # Создаём задачи для участников
    tasks = [start_strongman(name, power) for name, power in participants]

    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)


# Запуск соревнований
if __name__ == "__main__":
    asyncio.run(start_tournament())
