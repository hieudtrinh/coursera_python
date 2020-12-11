import sys
from typing import List


class DeleteColumnsToMakeSorted:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum(col != tuple(sorted(col)) for col in zip(*A))

    def minDeletionSize1(self, A: List[str]) -> int:

        res = 0
        for pos in range(len(A[0])):
            for word in range(len(A)-1):
                if A[word][pos] > A[word+1][pos]:
                    res += 1
                    break
        return res

    def minDeletionSize2(self, A: List[str]) -> int:
        strings = []
        for i in range(0,len(A[0])):
            temp = "".join([item[i] for item in A])
            if "".join(sorted(temp)) == temp:
                pass
            else:
                strings.append(1)
        return len(strings)

    def minDeletionSize3(self, A: List[str]) -> int:
        l=[]
        k=[]
        for i in range(len(A[0])):
            for j in range(len(A)):
                l.append((A[j][i]))
            if l != sorted(l):
                k.append(i)
            l=[]

        return len(k)



def main(argv, arc):
    A = ["cba", "daf", "ghi"]
    solution = DeleteColumnsToMakeSorted()
    solution.minDeletionSize(A)


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
