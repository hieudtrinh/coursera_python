from unittest import TestCase

from MinCostToMoveChips import MinCostToMoveChips


class Test(TestCase):
    def test_min_cost_to_move_chips(self):
        self.solution = MinCostToMoveChips()
        position = [2, 2, 2, 3, 3]
        self.assertEqual(self.solution.minCostToMoveChips(position), 2)
