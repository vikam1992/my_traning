# Импортируем необходимые модули
import unittest
import runner  # Импортируем модуль с классами Runner и Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Создаём общий атрибут для хранения всех результатов
        cls.all_results = {}

    def setUp(self):
        # Создаём объекты бегунов перед каждым тестом
        self.runner_1 = runner.Runner("Усэйн", speed=10)  # Быстрый бегун
        self.runner_2 = runner.Runner("Андрей", speed=9)  # Средний бегун
        self.runner_3 = runner.Runner("Ник", speed=3)  # Медленный бегун

    @classmethod
    def tearDownClass(cls):
        # Вывод всех результатов после выполнения всех тестов
        for test_name, result in cls.all_results.items():
            print(f"{test_name}: {result}")

    def test_runner_1(self):
        # Тест: Забег между Усэйном и Ником
        tournament = runner.Tournament(90, self.runner_1, self.runner_3)
        results = tournament.start()
        # Сохраняем результаты забега
        self.__class__.all_results["test_runner_1"] = {place: str(runner) for place, runner in results.items()}
        # Проверяем, что Ник всегда последний
        self.assertEqual(str(results[max(results)]), "Ник")

    def test_runner_2(self):
        # Тест: Забег между Андреем и Ником
        tournament = runner.Tournament(90, self.runner_2, self.runner_3)
        results = tournament.start()
        # Сохраняем результаты забега
        self.__class__.all_results["test_runner_2"] = {place: str(runner) for place, runner in results.items()}
        # Проверяем, что Ник всегда последний
        self.assertEqual(str(results[max(results)]), "Ник")

    def test_runner_3(self):
        # Тест: Забег между Усэйном, Андреем и Ником
        tournament = runner.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament.start()
        # Сохраняем результаты забега
        self.__class__.all_results["test_runner_3"] = {place: str(runner) for place, runner in results.items()}
        # Проверяем, что Ник всегда последний
        self.assertEqual(str(results[max(results)]), "Ник")
