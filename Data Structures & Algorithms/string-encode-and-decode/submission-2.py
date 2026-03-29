class Solution:

    def encode(self, strs) -> str:
        
        encoded_string = ""
        for i,string in enumerate(strs):
            for char in string:
                encoded_string = encoded_string + str(ord(char))
                encoded_string = encoded_string + "#"
            encoded_string+=";"
            
        return encoded_string
            
    def decode(self, s: str):
        return ["".join([chr(int(char)) for char in string.split("#") if char]) for string in s.split(";")][:-1] if s else []