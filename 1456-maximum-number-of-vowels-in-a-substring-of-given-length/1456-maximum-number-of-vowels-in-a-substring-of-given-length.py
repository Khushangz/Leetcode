class Solution(object):
    def maxVowels(self, s, k):
        vowel=["a","e","i","o","u"]
        count=0
        for i in s[0:k]:
            if i in vowel:
                count+=1
        curr_count=count
        for i in range(k,len(s)):
            if s[i-k] in vowel:
                curr_count-=1
            if s[i] in vowel:
                curr_count+=1
            count=max(curr_count,count)
        return count

        
        