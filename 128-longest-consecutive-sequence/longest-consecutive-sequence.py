class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=1
        nums= set(nums)
        if len(nums)==0:
         return 0
        for n in nums:
            if n-1 not in nums:
                if n+1 in nums:
                    j=2
                    c=2
                    while n+j in nums:
                        j+=1
                        c+=1
                    if count < c:
                        count=c
        return count
