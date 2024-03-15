class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cipher_key = []
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' , 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        for letter in key:
            if letter not in cipher_key and letter is not " ":
                cipher_key.append(letter)
        
        decoded_message = []
        for letter in message:
            if letter is ' ':
                decoded_message.append(' ')
            else:
                decoded_message.append(alphabet[cipher_key.index(letter)])
        
        return ''.join(decoded_message)


