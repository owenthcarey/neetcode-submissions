class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums_set = set(nums)
        for num in nums_set:
            current_streak = 1
            while num + 1 in nums_set:
                current_streak += 1
                num += 1
            if current_streak > longest_streak:
                longest_streak = current_streak
        return longest_streak
