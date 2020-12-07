from unittest import TestCase
from ArrayFormationThroughConcat import ArrayFormationThroughConcat


class TestArrayFormationThroughConcat(TestCase):
    def test_can_form_array(self):
        self.solution = ArrayFormationThroughConcat()
        arr = [49,18,16]
        pieces = [[16,18,49]]
        self.assertFalse(self.solution.canFormArray(arr, pieces))
        self.assertTrue(self.solution.canFormArray([91,4,64,78], [[78],[4,64],[91]]))
