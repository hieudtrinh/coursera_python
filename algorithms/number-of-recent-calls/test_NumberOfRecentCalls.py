from unittest import TestCase
from NumberOfRecentCalls import NumberOfRecentCalls


class TestNumberOfRecentCalls(TestCase):
    def test_ping(self):
        self.solution = NumberOfRecentCalls()
        print(self.solution.ping(1))
        print(self.solution.ping(100))
        print(self.solution.ping(3001))
        print(self.solution.ping(3002))
