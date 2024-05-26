class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = 'aeiouAEIOU'


        sentence = sentence.split(' ')
        for i in range(len(sentence)):
            if sentence[i][0] in vowels:
                sentence[i] = sentence[i] + 'ma'
            else:
                sentence[i] = sentence[i][1:] + sentence[i][0]
                sentence[i] += 'ma'
            for j in range(i+1):
                sentence[i] = sentence[i] + 'a'

        output = ''
        for word in sentence:
            output += word
            output += ' '
        return output[:len(output)-1]
        
