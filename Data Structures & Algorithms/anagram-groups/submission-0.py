class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through each srt for each str (n^2)
        # sort each str alphabetically, if target = this str, add them to same tuple
        result = []
        added = [0] * len(strs)
        for i in range(len(strs)):
            target = "".join(sorted(strs[i])) 
            miniResult = []
            if added[i] == 0:
                miniResult.append(strs[i])
                added[i] = 1
                for j in range(i, len(strs)):
                    candidate = "".join(sorted(strs[j]))
                    if target == candidate and added[j] == 0:
                        miniResult.append(strs[j])
                        added[j] = 1
                result.append(miniResult)
        return result




        