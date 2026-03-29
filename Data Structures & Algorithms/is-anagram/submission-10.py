class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approach #1

        1. Sort both strings and compare if they are equal.

        Approach #2

        1. Maintain constant space (26 length character array) frequency array.
        2. Loop over first string and keep on increasing character count based on
           ascii value of character. Could be found using python's ord function
        3. Loop over second string and this time rather subtract character account
           values in array
        4. If any place is left with a non zero would mean difference in count 
           digit making them non anagrams else False
            
        """

        if len(s) != len(t):
            return False

        # Implementing Approach #2
        count_array = [0]*26

        # First loop to increase count
        for char in s:
            count_array[ord(char) - ord('a')]+=1  #Subtracting ord('a') as a starting ref to place in array index

        # Second loop to decrease count
        for char in t:
            count_array[ord(char) - ord('a')]-=1

        # Last loop to check check for any non zero count in array
        for ele in count_array:
            if ele != 0: # Return False as count is not reduced to 0 for this posi
                return False

        # Return True if above loop did not find any non zero occurence 
        return True



        


        