class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for ele in nums:
            if (ele-1) not in nums_set:
                # If 1 left element not in nums_set means we can consider
                # it as a start of the sequence, So we start looking towards the right
                # We keep on looking for next num as per sequence till we dont find
                length = 1
                next_ele = ele + 1
                while next_ele in nums_set:
                    length+=1
                    next_ele+=1

                longest = max(longest, length)

        return longest

                




                




        