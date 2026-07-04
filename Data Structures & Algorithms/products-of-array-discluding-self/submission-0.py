class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        for i, num in enumerate(nums):
            result = 1
            for j, num in enumerate(nums):
                if i != j:
                    result *= num
            results.append(result)
        return results
