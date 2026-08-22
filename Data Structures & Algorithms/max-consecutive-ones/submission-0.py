class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        low = 0
        res = 0
        ans = 0
        
        for high in range(len(nums)):
            if nums[high] == 1:
                ans += 1
            else:
                ans = 0
                

            res = max(res,ans)

        return res