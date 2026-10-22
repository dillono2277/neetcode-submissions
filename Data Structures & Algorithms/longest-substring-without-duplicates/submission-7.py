class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxString = 0
        seen = set()

        l = 0
        for r in range(len(s)):
            if l == r:
                seen.add(s[r])
                continue
            if s[r] in seen:
                maxString = max(maxString, len(s[l:r]))
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
        if len(seen) != 0:
            maxString = max(maxString, len(seen))
            
        return maxString
