class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h=1
        p=0
        t=0
        d=10
        if(len(needle)>len(haystack)):
            return -1
        q=len(needle)+len(haystack)
        for i in range(len(needle)-1):
            h=(h*d)%q
        for i in range(len(needle)):
            t=(d*t+ord(haystack[i]))%q
            p=(p*d+ord(needle[i]))%q
        for i in range(len(haystack)-len(needle)+1):
            if p==t:
                count=0
                for j in range(len(needle)):
                    if(needle[j]!=haystack[j+i]):
                        break
                    count+=1
                if count==len(needle):
                    return i
            if i<len(haystack)-len(needle):
                t=(d*(t-ord(haystack[i])*h)+ord(haystack[i+len(needle)]))%q
                if(t<0):
                    t=t+q
        return -1
