from unittest import TestCase

from RemoveOuterMostParentheses import RemoveOuterMostParentheses


class TestRemoveOuterMostParentheses(TestCase):
    def test_remove_outer_parentheses(self):
        self.solution = RemoveOuterMostParentheses()
        S1 = "(()())(())"
        Ans1 = "()()()"

        S2 = "(()())(())(()(()))"
        Ans2 = "()()()()(())"

        self.assertEqual(self.solution.removeOuterParentheses(S1), Ans1)
        self.assertEqual(self.solution.removeOuterParentheses(S2), Ans2)
