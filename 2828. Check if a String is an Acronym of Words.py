class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acronym: List[str] = []
        acronym = (word[0] for word in words)
        return ''.join(acronym) == s
