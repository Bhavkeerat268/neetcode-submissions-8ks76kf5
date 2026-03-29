class Solution:

    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        character_array = [0]*26


        for char in s:
            character_array[ord(char) - ord('a')]+=1

        for char in t:
            character_array[ord(char) - ord('a')]-=1

        print(character_array)

        for i in character_array:
            if i>0:
                return False

        return True



        