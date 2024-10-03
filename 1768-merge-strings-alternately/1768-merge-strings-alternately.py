class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string=""
        flag=0
        if len(word1)>len(word2):
            max=len(word2)
            flag=1
        else:
            max=len(word1)
        for i,x in zip(word1,word2):
            string+=i+x
        if flag==1:
            for i in word1[max:]:
                string+=i
        else:  
            for i in word2[max:]:
                string+=i
        return(string)
        
        

