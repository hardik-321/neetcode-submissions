class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_length = len(strs)
        ans = ""
        letter = ""
        a = strs[0]
        a_length = len(a)
        c = ""
        for n in range(0 , a_length):
            letter = a[n]
            for i in range(1 , strs_length):
                c = strs[i]
                if c == "":
                    return ans
                if n >= len(c):
                    return ans
                if letter == c[n]:
                    letter = letter
                else:
                    return ans
            ans += letter
        return ans
                