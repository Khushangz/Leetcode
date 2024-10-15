class Solution:
    def compress(self, chars: List[str]) -> int:
        w=0
        r=0
        count=0
        while r<len(chars):
            if chars[r]==chars[w]:
                count+=1
                r+=1
            else:
                if count>1:
                    if count>=10:
                        count=str(count)
                        for x in count:
                            chars[w+1]=x
                            w+=1
                    else:
                        chars[w+1]=str(count)
                        w+=1
                chars[w+1]=chars[r]
                w+=1
                count=1
                r+=1
        if count>1:
            if count>=10:
                count=str(count)
                for x in count:
                    chars[w+1]=x
                    w+=1
            else:
                chars[w+1]=str(count)
                w+=1
        return(w+1)

        

            
        