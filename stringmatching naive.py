class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        temp=-1
        for i in range(len(haystack)-len(needle)+1):
            count=0
            while(count<len(needle)):
                if haystack[count+i]!=needle[count]:
                    break
                count+=1
            if count==len(needle):
                return i
        return temp    
