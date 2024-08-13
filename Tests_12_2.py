# Изменения в классе Runner:
# Появился атрибут speed для определения скорости бегуна.
# Метод __eq__ для сравнивания имён бегунов.
# Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
# Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и
# список участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции.
#
# Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
#
# setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут
# сохраняться результаты всех тестов.
# setUp - метод, где создаются 3 объекта:
# Бегун по имени Усэйн, со скоростью 10.
# Бегун по имени Андрей, со скоростью 9.
# Бегун по имени Ник, со скоростью 3.
# tearDownClass - метод, где выводятся all_results по очереди в столбец.
#
# Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
#  У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results.
# В конце вызывается метод assertTrue, в котором сравниваются последний объект из all_results
# (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
# Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
# Усэйн и Ник
# Андрей и Ник
# Усэйн, Андрей и Ник.
# Как можно понять: Ник всегда должен быть последним.



import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}



    def setUp(self):
        self.atlet1 = runner_and_tournament.Runner('Усэйн', 10)
        self.atlet2 = runner_and_tournament.Runner('Андрей', 9)
        self.atlet3 = runner_and_tournament.Runner('Ник', 3)

    def tearDown(self):
        print(self.all_results)



    def test_runner_1(self):
        test_1 = runner_and_tournament.Tournament(90, self.atlet1, self.atlet3)
        dict_1 = test_1.start()
        self.assertTrue(dict_1[2], self.atlet3)
        self.all_results.update(dict_1)
        #print(self.all_results)



    def test_runner_2(self):
        test_2 = runner_and_tournament.Tournament(90, self.atlet2, self.atlet3)
        dict_2 = test_2.start()
       
        self.assertTrue(dict_2[2], self.atlet3)
        self.all_results.update(dict_2)


    def test_runner_3(self):
        test_3 = runner_and_tournament.Tournament(90, self.atlet1, self.atlet2, self.atlet3)
        dict_3 = test_3.start()
        self.all_results.update(dict_3)
        self.assertTrue(dict_3[3], self.atlet3)


if __name__ == '__main__':
    unittest.main()






