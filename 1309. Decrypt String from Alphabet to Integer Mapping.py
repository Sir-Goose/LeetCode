class Solution:
    def freqAlphabets(self, s: str) -> str:
        tokens = []
        key = {'1': 'a',
        '2': 'b',
        '3': 'c',
        '4': 'd',
        '5': 'e',
        '6': 'f',
        '7': 'g',
        '8': 'h',
        '9': 'i',
        '10#': 'j',
        '11#': 'k',
        '12#': 'l',
        '13#': 'm',
        '14#': 'n',
        '15#': 'o',
        '16#': 'p',
        '17#': 'q',
        '18#': 'r',
        '19#': 's',
        '20#': 't',
        '21#': 'u',
        '22#': 'v',
        '23#': 'w',
        '24#': 'x',
        '25#': 'y',
        '26#': 'z'}



        i = 0  
        while True:
            try:

                if s[i + 2] == '#':
                    tokens.append(s[i: i + 3])
                    s = s[i + 3:]
                    print(s)
                    i = 0
                else:
                    tokens.append(s[i])
                    s = s[i + 1:]
                    i = 0
            except:
                tokens.append(s[i])
                s = s[i + 1:]
                i = 0
            if len(s) == 0:
                break
            

        print(s)
        print(tokens)

        for i in range(len(s)):
            tokens.append(s[i])

        print(tokens)

        result = ""
        for token in tokens:
            result += key[token]
        print(result)
        return result

