class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openn, closed):
            if openn == closed == n:
                res.append("".join(stack))
                return
            if openn < n:
                stack.append("(")
                backtrack(openn + 1, closed)
                stack.pop()
            if closed < openn:
                stack.append(")")
                backtrack(openn, closed + 1)
                stack.pop()

        backtrack(0, 0)
        return res
