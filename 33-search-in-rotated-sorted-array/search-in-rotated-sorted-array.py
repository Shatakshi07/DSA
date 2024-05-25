class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_ptr = 0
        right_ptr = len(nums) -1
        left_val = nums[0]
        right_val = nums[right_ptr]
        while left_ptr <= right_ptr:
            mid_ptr = (left_ptr + right_ptr) // 2
            mid_val = nums[mid_ptr]
            # print(left_ptr, right_ptr, mid_ptr)
            if mid_val == target: return mid_ptr
            elif mid_val >= left_val:
                if target >= left_val and target < mid_val:
                    right_ptr = mid_ptr - 1
                    right_val = nums[right_ptr]
                else:
                    if mid_ptr < len(nums)-1:
                        left_ptr = mid_ptr + 1  
                    else:
                        return -1
                    left_val = nums[left_ptr]

            else:
                if target > mid_val and target <= right_val:
                        if mid_ptr < len(nums)-1:
                            left_ptr = mid_ptr + 1  
                        else:
                            return -1
                        left_val = nums[left_ptr]
                else:
                    if mid_ptr > 0:
                        right_ptr = mid_ptr - 1
                    else:
                        return -1
                    right_val = nums[right_ptr]
        return -1