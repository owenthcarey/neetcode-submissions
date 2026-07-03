class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_dict = {}
        for string in strs:
            string_array = []
            for character in string:
                string_array.append(character)
            string_array.sort()
            if not ''.join(string_array) in string_dict:
                string_dict[''.join(string_array)] = [string]
            else:
                string_dict[''.join(string_array)].append(string)
        output_list = []
        for key in string_dict.keys():
            output_list.append(string_dict[key])
        return output_list
