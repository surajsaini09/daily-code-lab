class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        freq = {}

        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0 ) + 1

            if right - left > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            if freq[nums[right]] > 1:
                return True
        return False 
