from unittest import TestCase
from ReplaceElementsWithGreatestElementOnRightSide import ReplaceElementsWithGreatestElementOnRightSide


class Test(TestCase):
    def test_replace_elements_with_greatest_element_on_right_side(self):
        self.solution = ReplaceElementsWithGreatestElementOnRightSide()
        arr = [17,18,5,4,6,1]
        print(arr)
        arr2 = self.solution.replaceElements(arr)
        print(arr2)