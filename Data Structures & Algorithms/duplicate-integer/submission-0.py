class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {num : 0 for num in nums}
        for num in nums:
            nums_dict[num] = nums_dict[num] + 1

        has_duplicate = False
        for key, value in nums_dict.items():
            if value > 1:
                has_duplicate = True

        return has_duplicate
