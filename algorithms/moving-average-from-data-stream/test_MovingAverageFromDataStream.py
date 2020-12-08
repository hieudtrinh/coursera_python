from unittest import TestCase

from MovingAverageFromDataStream import MovingAverageFromDataStream


class TestMovingAverageFromDataStream(TestCase):
    def test_next(self):
        self.solution = MovingAverageFromDataStream(3)
        arr = [1, 10, 3, 5]
        for n in arr:
            print(self.solution.next(n))
