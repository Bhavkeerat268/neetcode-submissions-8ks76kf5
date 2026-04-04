class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            while left < right and not self.checkIsValidChar(s[left]):
                left+=1

            while left < right and not self.checkIsValidChar(s[right]):
                right-=1


            if s[left].lower()!=s[right].lower():
                return False

            left+=1
            right-=1


        return True

    def checkIsValidChar(self, char):
        if ord(char) <= ord('z') and ord(char) >= ord('a'):
            return True

        if ord(char) <= ord('Z') and ord(char) >= ord('A'):
            return True

        if ord(char) <= ord('9') and ord(char) >= ord('0'):
            return True

        return False
        

