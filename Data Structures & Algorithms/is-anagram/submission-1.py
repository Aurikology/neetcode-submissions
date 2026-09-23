## two components to solve for. 
## 1. The length of the string
## 2. The characters of the string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ## create Hashmap to count the characters in both of the strings    
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        for c in countS: ## c is the key that is iterating between the hashmap
            if countS[c]!= countT.get(c,0):
                return False
        return True

        