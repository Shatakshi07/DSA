class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # create a deque to hold the indices of the elements in the sliding window
        window = deque()
        result = []
        
        # iterate through the array
        for i in range(len(nums)):
            # remove elements from the deque that are outside the window
            while window and window[0] <= i - k:
                window.popleft()
            
            # remove elements from the deque that are smaller than the current element
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            # add the index of the current element to the deque
            window.append(i)
            
            # add the maximum element in the window to the result list
            if i >= k - 1:
                result.append(nums[window[0]])
        
        return result


    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        m=min(nums)
        idx=0
        for i in range(k):
            if m< nums[i]:
                m=nums[i]
                idx=i
        print(m)
        print(idx)
        out=[]
        out.append(m)
        j=1
        window=1
        for i in range(1 , len(nums)-k+1):
            window+=1
            if idx<i:
                m=nums[i]
                for j in range(i,i+k):
                    if m< nums[j]:
                        m=nums[j]
                        idx=j
            elif m<nums[i+k-1]:
                idx=i+k-1
                m=nums[i+k-1]
            out.append(m)
        return out



