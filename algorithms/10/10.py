# Use classes to represent regular expressions and recursion to match the string against the regular expression. 
# The regular expression is constructed from the pattern string, where each character is represented as a Char object, except for "." which is represented with an AnyChar and the '*' character is represented as a RepeatingChar object. 
# The recursiveMatch function takes a regular expression and a string, and returns a set of indices in the string that match the regular expression. 
# The isMatch function constructs the regular expression from the pattern and then checks if the length of the string is in the set of matching indices.

class Regex:
    pass

class Char(Regex):
    def __init__(self, c):
        self.c = c

class AnyChar(Regex):
    pass

class RepeatingChar(Regex):
    def __init__(self, r):
        self.r = r

class Concat(Regex):
    def __init__(self, left, right):
        self.left = left
        self.right = right


regex_dico = {}


class Solution:
    def reduceExpression(self, p: str) :
        n = len(p)
        i = 0
        res = ""
        while(i < n) :
            current = p[i]
            next = None
            if i + 1 < n :
                next = p[i + 1]

            res += current

            if next == "*" :
                k = i + 2
                res += next
                while k < n and p[k] == current and k + 1 < n and p[k + 1] == "*" :
                    k += 2
                i = k
            else :
                i += 1

        return res


    def toRegex(self, s: str, i = 0) :
        n = len(s) 
        k = i + 1

        if k < n and s[k] == "*" : 
            k = i + 2
            if s[i] == "." :
                regex = RepeatingChar(AnyChar())
            else :
                regex = RepeatingChar(Char(s[i]))
        elif s[i] == "." :
            regex =  AnyChar()
        else :
            regex = Char(s[i])

        if k == n : return regex

        return Concat(regex, self.toRegex(s,k))

    def recursiveMatch(self, regex: Regex, s: str, i = 0) -> set[int]:
        key = (id(regex), i)
        if key in regex_dico:
            return regex_dico[key]
        
        match regex :
            case Char(c = c) :
                if i < len(s) and s[i] == c :
                    regex_dico[key] = {i + 1}
                else :
                    regex_dico[key] = set()
                return regex_dico[key]
            
            case AnyChar() :
                if i >= len(s) :
                    regex_dico[key] = set()
                else :
                    regex_dico[key] = {i + 1}
                return regex_dico[key]
            
            case RepeatingChar(r = r) :
                result = {i} # No repeat
                indexes = self.recursiveMatch(r, s, i) # Repeat once
                possible_indexes = [j for j in indexes if j > i]
                for j in possible_indexes :
                    result.update(self.recursiveMatch(regex,s,j)) # Try to reapeat more at every positions
                regex_dico[key] = result
                return result

            case Concat(left = l, right = r) :
                indexes = self.recursiveMatch(l, s, i)
                result = set()
                for k in indexes :
                    result.update(self.recursiveMatch(r,s,k))
                regex_dico[key] = result
                return result
        
        return set()


    def isMatch(self, s: str, p: str) -> bool:
        # Clear dictionnary
        regex_dico.clear()

        # Reduce the string expression
        p = self.reduceExpression(p)

        # Construction of the regular expression
        regex = self.toRegex(p)

        # Pattern Matching
        result = self.recursiveMatch(regex, s)
        print(result)

        return (len(s) in result)