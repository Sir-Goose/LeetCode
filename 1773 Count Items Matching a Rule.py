class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        print(items)
        rule: int = -1
        match ruleKey:
            case "type":
                rule = 0
            case "color":
                rule = 1
            case "name":
                rule = 2

        match_count: int = 0
        
        for item in items:
            if item[rule] == ruleValue:
                match_count += 1
        
        return match_count
                
