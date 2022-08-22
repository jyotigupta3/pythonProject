class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub_str = s[i:j]
                l = len(set(sub_str))
                if len(sub_str) == l:
                    
                    if len(result) < l:
                        result = sub_str
        print(len(result))
        print(result)
        return len(result)
