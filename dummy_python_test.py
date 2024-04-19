"""Выполните тестовое задание, чтобы мы понимали уровень вашей подготовки. """

from collections import Counter
import math


def get_unique_integers_from_list(arr: list[int]) -> list[int]:
    """
    Функция, которая принимает на вход список целых чисел
    и возвращает новый список,
    содержащий только уникальные элементы из исходного списка.
    """

    result = []
    for key, val in Counter(arr).items():
        if val == 1:
            result.append(key)
    return result


def get_primes_range(min_prime: int, max_prime: int) -> list[int]:
    """
    Функция, которая принимает на вход два целых числа (минимум и максимум)
    и возвращает список всех простых чисел в заданном диапазоне.
    """

    primes = set([*range(2, max_prime + 1)])
    for num in range(2, math.ceil(max_prime**0.5)):
        if num in primes:
            primes -= set(range(num * 2, max_prime + 1, num))
    result = sorted(filter(lambda x: x >= min_prime, primes))
    return result


class Point:
    """
    Класс Point, который представляет собой точку в двумерном пространстве.
    Класс должен иметь методы для:
        - инициализации координат точки
        - вычисления расстояния до другой точки
        - для получения и изменения координат
    """

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @staticmethod
    def validate_coord(val):
        if type(val) in (int, float):
            return
        raise ValueError(f"Incorrect value: {val}  for coordinates")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.validate_coord(val)
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.validate_coord(val)
        self.__y = val

    def get_coords(self) -> tuple[int, int]:
        return self.__x, self.__y

    def get_distance(self, obj: "Point") -> float:
        if not isinstance(obj, Point):
            raise TypeError("You can use only other Point objects to get distance")
        return math.dist(self.get_coords(), obj.get_coords())


def sort_strings_by_length(strings: list[str], reverse: bool = False):
    """
    Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.
    """
    return sorted(strings, key=len, reverse =reverse)


if __name__ == "__main__":
    import unittest

    class Tests(unittest.TestCase):

        def test_unique_integers(self):
            self.assertEqual(get_unique_integers_from_list([1, 2, 3]), [1, 2, 3])
            self.assertEqual(get_unique_integers_from_list([1, 1, 1]), [])
            self.assertEqual(get_unique_integers_from_list([]), [])
            self.assertEqual(
                get_unique_integers_from_list([1, 1, 1, 2, 3, 1, 4, 4]), [2, 3]
            )

        def test_primes_range(self):
            self.assertEqual(get_primes_range(1, 15), [2, 3, 5, 7, 11, 13])
            self.assertEqual(get_primes_range(0, 1), [])

        def test_string_len_sorter(self):
            strings = ["a", "aaa", "aa"]
            self.assertEqual(sort_strings_by_length(strings), ["a", "aa", "aaa"])
            self.assertEqual(
                sort_strings_by_length(strings, reverse=True), ["aaa", "aa", "a"]
            )

    class PointTests(unittest.TestCase):

        def test_point_setters_getters(self):
            point = Point(x=1, y=2)

            self.assertEqual(point.get_coords(), (1, 2))

            point.x = 2
            point.y = 3
            self.assertEqual(point.get_coords(), (2, 3))

            with self.assertRaises(ValueError):
                point.x = "1"

        def test_distance_measure(self):
            point = Point(x=1, y=1)

            h_shifted_point = Point(x=2, y=1)
            self.assertEqual(point.get_distance(h_shifted_point), 1)

            v_shifted_point = Point(x=1, y=2)
            self.assertEqual(point.get_distance(v_shifted_point), 1)

            d_shifted_point = Point(2, 2)
            self.assertAlmostEqual(point.get_distance(d_shifted_point), 1.4142135623731)

            with self.assertRaises(TypeError):
                point.get_distance((1, 2))

        def test_distance_not_negative(self):
            point = Point(x=1, y=1)

            neg_shifted_point = Point(0, 0)
            self.assertAlmostEqual(
                point.get_distance(neg_shifted_point), 1.4142135623731
            )

    unittest.main()
