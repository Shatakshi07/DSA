class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        
        for i in range(len(nums)):
            if d.get(nums[i]) is not None:
                return nums[i]
            d[nums[i]]=i
            #print(d)
        #print(d)
        return -1
