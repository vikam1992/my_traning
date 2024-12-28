import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walking = runner.Runner('Rita') # создание объекта класса Runner с именем
        for i in range(10):
            walking.walk() # вызываем функцию 10 раз
        self.assertEqual(walking.distance, 50)

    def test_run(self):
        running = runner.Runner('Rose')
        for i in range(10):
            running.run()
        self.assertEqual(running.distance, 100)

    def test_challenge(self):
        walking_2 = runner.Runner('Martha')
        running_2 = runner.Runner('Peter')
        for i in range(10):
            walking_2.walk(), running_2.run()
        self.assertNotEqual(walking_2.distance, running_2.distance)


if __name__ == '__main__':
    unittest.main()
