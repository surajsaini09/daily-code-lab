class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        left = 0
        freq = {}

        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right],0) + 1

            if freq[nums[right]] > 1:
                return True
        return False