class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach #1

        1. Use two nested loops, First goes till less than len(nums) - 1
        2. Second one goes till less than len(nums)
        3. Check if nums[i] and nums[j] makes target. If yes return i, j pair
        
        Approach #2

        1. Maintain a dictionary or a count array which will store the value
           and the corresponding position in the array,
        2. Iterate over the array and do a target - nums[i] computation and
           look for this result in your dictionary you maintained in step 1
        3. If that exists, then you got another number in array which would
           make up to your target else simply insert that in your dict
           with the array index value. So nums[i] as key and index as value.
        
        """

        posi_dict = {}

        for i, ele in enumerate(nums):
            search_element = target - ele

            if search_element in posi_dict:
                return [posi_dict[search_element],i] # Return min index first
            
            posi_dict[ele] = i

            






        