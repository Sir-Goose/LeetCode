class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split(' ')

        prev = -1
        for token in s:
            if token.isdigit():
                if int(token) <= int(prev):
                    return False
                else:
                    prev = token
        return True

