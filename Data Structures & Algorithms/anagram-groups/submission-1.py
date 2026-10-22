class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        matches = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            if tuple(count) in matches:
                matches[tuple(count)].append(s)
            else:
                matches[tuple(count)] = [s]
        
        for key, value in matches.items():
            result.append(value)
        return result

                    