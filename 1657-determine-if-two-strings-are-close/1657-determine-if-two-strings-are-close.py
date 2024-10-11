class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1={}
        dict2={}

        if len(word1)!=len(word2):
            return False
        for i,a in zip(word1,word2):
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
            if a in dict2:
                dict2[a]+=1
            else:
                dict2[a]=1

        if sorted(dict1.values())==sorted(dict2.values()) and set(dict1.keys())==set(dict2.keys()):
            return True
        else:
            return False