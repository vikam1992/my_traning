import unittest
import runner  # Импортируем модуль с классами Runner и Tournament


def freeze_check(method):
    """
    Декоратор для проверки заморозки тестов.
    Если is_frozen=True, тест пропускается.
    """
    def wrapper(self, *args, **kwargs):
        if getattr(self, "is_frozen", False):
            self.skipTest("Тесты в этом кейсе заморожены")
        return method(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False  # Флаг, определяющий, заморожены ли тесты

    @freeze_check
    def test_run(self):
        """
        Тестирует метод run для бегуна.
        Проверяет, что расстояние увеличивается правильно.
        """
        r = runner.Runner("John", speed=10)
        r.run()
        self.assertEqual(r.distance, 20)

    @freeze_check
    def test_walk(self):
        """
        Тестирует метод walk для бегуна.
        Проверяет, что расстояние увеличивается правильно.
        """
        r = runner.Runner("John", speed=5)
        r.walk()
        self.assertEqual(r.distance, 5)

    @freeze_check
    def test_challenge(self):
        """
        Тестирует комбинацию методов run и walk.
        """
        r = runner.Runner("John", speed=8)
        r.run()
        r.walk()
        self.assertEqual(r.distance, 24)


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Флаг, определяющий, заморожены ли тесты

    @classmethod
    def setUpClass(cls):
        """
        Инициализация общего хранилища результатов для всех тестов.
        """
        cls.all_results = {}

    def setUp(self):
        """
        Инициализация объектов бегунов перед каждым тестом.
        """
        self.runner_1 = runner.Runner("Усэйн", speed=10)
        self.runner_2 = runner.Runner("Андрей", speed=9)
        self.runner_3 = runner.Runner("Ник", speed=3)

    @freeze_check
    def test_runner_1(self):
        """
        Тест турнира с участниками Усэйном и Ником.
        Проверяет, что Ник всегда последний.
        """
        tournament = runner.Tournament(90, self.runner_1, self.runner_3)
        results = tournament.start()
        TournamentTest.all_results["test_runner_1"] = {place: str(runner) for place, runner in results.items()}
        self.assertEqual(str(results[max(results)]), "Ник")

    @freeze_check
    def test_runner_2(self):
        """
        Тест турнира с участниками Андреем и Ником.
        Проверяет, что Ник всегда последний.
        """
        tournament = runner.Tournament(90, self.runner_2, self.runner_3)
        results = tournament.start()
        TournamentTest.all_results["test_runner_2"] = {place: str(runner) for place, runner in results.items()}
        self.assertEqual(str(results[max(results)]), "Ник")

    @freeze_check
    def test_runner_3(self):
        """
        Тест турнира с участниками Усэйном, Андреем и Ником.
        Проверяет, что Ник всегда последний.
        """
        tournament = runner.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = tournament.start()
        TournamentTest.all_results["test_runner_3"] = {place: str(runner) for place, runner in results.items()}
        self.assertEqual(str(results[max(results)]), "Ник")

    @classmethod
    def tearDownClass(cls):
        """
        Вывод результатов всех тестов после их завершения.
        """
        for test_name, result in cls.all_results.items():
            print(f"{test_name}: {result}")
