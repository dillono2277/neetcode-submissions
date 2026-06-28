class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1occ = {}
        s2occ = {}
        l = 0 
        r = len(s1) - 1


        for i in range(len(s1)):
            if s1[i] in s1occ:
                s1occ[s1[i]] +=1
            else:
                s1occ[s1[i]] = 1

            if s2[i] in s2occ:
                s2occ[s2[i]] +=1
            else:
                s2occ[s2[i]] = 1
        print("s1occ:")
        print(s1occ)
        print("s2occ")
        print(s2occ)

        #check if first substring is equal
        if s1occ == s2occ:
                return True
        #move to next substring
        if s2occ[s2[l]] > 1:
                s2occ[s2[l]] -= 1
        else:
            s2occ.pop(s2[l])
        l+=1
        r+=1
        
        while r < len(s2):
            #updating s2occ
            if s2[r] in s2occ:
                s2occ[s2[r]] += 1
            else:
                s2occ[s2[r]] = 1
            print("new map:")
            print(s2occ)
            #check if equal
            if s2occ == s1occ:
                return True
            #update pointers
            if s2occ[s2[l]] > 1:
                s2occ[s2[l]] -= 1
            else:
                s2occ.pop(s2[l])
            l+=1
            r+=1
        return False
            

            
            
            

       
        