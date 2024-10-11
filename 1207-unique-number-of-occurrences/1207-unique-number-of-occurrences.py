class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1={}
        for i in arr:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1

        if len(set(dict1.values()))!=len(dict1.values()):
            return False
        else:
            return True
