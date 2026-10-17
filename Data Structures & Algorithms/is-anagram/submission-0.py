class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for i in s:
            if i not in ds:
                ds[i] = 1
            else:
                ds[i] += 1
        for i in t:
            if i not in dt:
                dt[i] = 1
            else:
                dt[i] += 1   
        return ds == dt
        # for i in s:
        #     if ds[i] == dt[i]:
        #         return True
        #     else:
        #         return False