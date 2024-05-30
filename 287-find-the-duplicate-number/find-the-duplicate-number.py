class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break

        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow

        




    def BRUTEfindDuplicate(self, nums: List[int]) -> int:
        d={}
        
        for i in range(len(nums)):
            if d.get(nums[i]) is not None:
                return nums[i]
            d[nums[i]]=i
            #print(d)
        #print(d)
        return -1
