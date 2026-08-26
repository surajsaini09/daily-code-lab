class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        freq = {0 : 1}
        res = 0

        for i in range(len(nums)):
            total += nums[i]
            need = total - k

            if need in freq:
                res += freq[need]
            freq[total] = freq.get(total,0) + 1
        return res 
