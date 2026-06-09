close_brackets ={
    "(" : ")",
    "[" : "]",
    "{" : "}"
}

keys = ["(","[","{"]

class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        i = 0
        stack = []

        while(i < n) :
            match s[i] :
                case "(" | "[" | "{" :
                    stack.append(s[i])
                case ")" | "]" | "}" :
                    if stack == [] : return False
                    last = stack.pop()
                    if not(last in keys) or close_brackets[last] != s[i] :
                        return False
            i += 1
            
        return len(stack) == 0
    
