import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создание TestSuite
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(RunnerTest))  # Добавляем RunnerTest в TestSuite
suite.addTest(unittest.makeSuite(TournamentTest))  # Добавляем TournamentTest в TestSuite

# Запуск TestSuite
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
