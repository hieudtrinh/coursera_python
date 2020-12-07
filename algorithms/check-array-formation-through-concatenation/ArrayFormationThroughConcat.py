from typing import List


class ArrayFormationThroughConcat:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for piece in pieces:
            if piece[0] not in arr:
                return False
            index = arr.index(piece[0])
            if arr[index:index+len(piece)] != piece:
                return False
        return True