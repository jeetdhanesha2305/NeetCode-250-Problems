class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        charFreq = {}

        for char in s:
            if char in charFreq: 
                charFreq[char] += 1
            else:
                charFreq[char] = 1
        
        for char in t:
            if char in charFreq:
                charFreq[char] -= 1
                if charFreq[char] == 0:
                    del charFreq[char] 
            else:
                return False 
        
        return len(charFreq) == 0

        

        