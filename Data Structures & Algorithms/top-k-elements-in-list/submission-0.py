class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_dict = {}
        for num in nums:
            if num not in counter_dict:
                counter_dict[num] = 1
            else:
                counter_dict[num] += 1
        output_list = []
        for i, key in enumerate(sorted(counter_dict, key=counter_dict.get, reverse=True)):
            if i < k:
                output_list.append(key)
            else:
                break
        return output_list
