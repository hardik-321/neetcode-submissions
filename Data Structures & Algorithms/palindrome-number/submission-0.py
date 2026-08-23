class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = 0
        original = x

        while x > 0:
            a = x % 10

            ans = (ans*10) + a

            x = x//10
        return original == ans