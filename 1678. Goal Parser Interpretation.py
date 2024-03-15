class Solution:
    def interpret(self, command: str) -> str:
        parse: str = command.replace('G', 'G').replace('()', 'o').replace('(al)', 'al')
        
        return parse
