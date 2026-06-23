import re

class Solution:
    def isNumber(self, s: str) -> bool:
        integer = r"(\+|-)?\d+"
        fraction = r"(\+|-)?\d*[.]\d*"
        exponent = r"((e|E)(\+|-)\d*)"

        regex = "(" + integer + "|" + fraction + ")" + exponent + "?" 
        return bool(re.fullmatch(regex, s))