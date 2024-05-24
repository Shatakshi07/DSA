class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid=0
        def bs(i,j)-> int:
            if (i<=j):
                mid=int((i+j))//2
                if target==nums[mid] :
                    return mid
                elif target<nums[mid]:
                    return bs(i,mid-1)
                else:
                    return bs(mid+1,j)
            else:
                return -1
        mid=bs(0,len(nums)-1)
        return mid

            
