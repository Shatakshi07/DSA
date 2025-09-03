class Solution: # Kadane's Algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        currsum = 0

        for i, n in enumerate(nums):
            if currsum == 0:
                start =i

            currsum += n
            
            if currsum > maxsum :
                maxsum = currsum  
                end=i

            if currsum < 0:
                currsum=0


            
        return maxsum

    



        