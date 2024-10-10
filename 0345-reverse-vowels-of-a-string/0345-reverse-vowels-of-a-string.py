class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=["a","e","i","o","u","A","E","I","O","U"]
        ind=[]
        s=list(s)
        for i in range(len(s)):
            if s[i] in vowel:
                ind.append(i)
        for i in range(len(ind)//2):
            s[ind[len(ind)-i-1]],s[ind[i]]=s[ind[i]],s[ind[len(ind)-i-1]]

        return "".join(s)


       
        
            
       
# only vowels
# no vowels
# odd number of vowels
# even number
# sentences