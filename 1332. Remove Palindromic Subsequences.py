class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # either already a palindrome
        # or two steps.
        is_palindrome = True

        t = s[::-1]
        for i in range(len(s)):
            if s[i] != t[i]:
                is_palindrome = False

        return 1 if is_palindrome else 2

