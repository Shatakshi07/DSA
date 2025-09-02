class Solution:
    def minOperations(self, n: int) -> int:

        pows = [1 << i for i in range(int(log2(n))+2)]
        # 1 << i means "1 shifted left by i bits" = 2^i
        # range has +2 so that one more power of 2 is included

        ops = 0

        while n:
            closest = min(pows, key=lambda p: abs(n-p))
            # min goes through each element of pows one by one.
            # Each element is temporarily assigned to p, then passed into the lambda function.
            n = abs(n-closest)
            ops += 1

        return ops

# lambda arguments: expression
# It works just like a normal function, but it’s written in a single line.