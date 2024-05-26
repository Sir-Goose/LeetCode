class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        output = []
        for word in words:
            segments = word.split(separator)
            for segment in segments:
                if len(segment) > 0:
                    output.append(segment)
        return output

