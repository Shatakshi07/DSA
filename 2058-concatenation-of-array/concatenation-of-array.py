class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)  # Extend the list with itself
        return nums       