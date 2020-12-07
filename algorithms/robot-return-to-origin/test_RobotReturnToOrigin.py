from unittest import TestCase

from RobotReturnToOrigin import RobotReturnToOrigin


class TestRobotReturnToOrigin(TestCase):
    def test_judge_circle(self):
        self.solution = RobotReturnToOrigin()
        self.assertTrue(self.solution.judgeCircle("UDLRUUDD"))
