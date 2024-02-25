class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse: List[str] = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        codes: List[str] = []

        for word in words:
            morse_code = ""
            for char in word:
                morse_code += morse[ord(char) - ord('a')]
            if morse_code not in codes:
                codes.append(morse_code)
        
        return len(codes)

