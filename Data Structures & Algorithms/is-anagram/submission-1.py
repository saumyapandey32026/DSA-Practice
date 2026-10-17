class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ds = {}
        # dt = {}
        # for i in s:
        #     if i not in ds:
        #         ds[i] = 1
        #     else:
        #         ds[i] += 1
        # for i in t:
        #     if i not in dt:
        #         dt[i] = 1
        #     else:
        #         dt[i] += 1   
        # return ds == dt

        
        if len(s) != len(t):
            return False
            
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] == 0:
                del count[char] 
        return len(count) == 0

    