class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k > len(s):
            return len(s)
        freqDict = {}
        result = 0

        l = 0

        for r in range(len(s)):
            if s[r] in freqDict:
                freqDict[s[r]] += 1
            else:
                freqDict[s[r]] = 1
            numOfReplace = (r+1 - l) - max(freqDict.values())

            while numOfReplace > k:
                freqDict[s[l]] -= 1
                l+= 1
                numOfReplace = (r+1 - l) - max(freqDict.values())
            result = max(result, (r+1 - l))
        return result
            


        
        