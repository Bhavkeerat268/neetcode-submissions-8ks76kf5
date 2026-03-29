class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_sublists_positions = {}
        output = []

        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string not in anagram_sublists_positions:
                anagram_sublists_positions[sorted_string] = len(output)
                output.append([])
            
            output[anagram_sublists_positions[sorted_string]].append(string)

        return output

        