class RemoveOuterMostParentheses:
    def removeOuterParentheses(self, S: str) -> str:
        depth = 0
        ans = ""
        for c in S:
            if c == '(':
                if depth > 0:
                    ans += c
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    ans += c
        return ans
