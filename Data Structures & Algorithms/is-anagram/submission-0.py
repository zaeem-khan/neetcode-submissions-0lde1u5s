class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCharMap = {}
        for ch in s:
            if sCharMap.get(ch):
                sCharMap[ch] += 1
            else:
                sCharMap[ch] = 1
        
        for ch in t:
            if sCharMap.get(ch):
                sCharMap[ch] -= 1
            else:
                return False

        return all(value == 0 for value in sCharMap.values())