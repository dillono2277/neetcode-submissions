class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        dupes = set()
        longestInt = 0

        for right in range(len(s)):
            while s[right] in dupes:
                dupes.remove(s[left])
                left+= 1
            dupes.add(s[right])
            longestInt = max(longestInt, right - left + 1)
        return longestInt




  

        # while right <= len(s):
        #     while s[left] in dupes:
        #         dupes.remove(s[left])
        #         left+=1       
        #     else:
        #         longestInt = max(longestInt, right - left + 1)
        #         dupes.add(right)
        #         right += 1
        # return longestInt





        