from unittest import TestCase
from DeleteColumnsToMakeSorted import DeleteColumnsToMakeSorted


class Test(TestCase):
    def test_main(self):
        self.solution = DeleteColumnsToMakeSorted()
        A = ["zyx","wvu","tsr"]
        print(self.solution.minDeletionSize(A))
        print(self.solution.minDeletionSize1(A))
        print(self.solution.minDeletionSize2(A))
        print(self.solution.minDeletionSize3(A))

