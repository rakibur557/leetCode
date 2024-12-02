class Solution(object):
    def isNumber(self, s):
        def isInteger(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            return s.isdigit()
        
        def isDecimal(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            if '.' not in s:
                return False
            integer_part, dot, fractional_part = s.partition('.')
            if not integer_part and not fractional_part:
                return False
            if integer_part and not integer_part.isdigit():
                return False
            if fractional_part and not fractional_part.isdigit():
                return False
            return True
        
        def isExponent(s):
            if 'e' not in s and 'E' not in s:
                return False
            base, _, exponent = s.partition('e') if 'e' in s else s.partition('E')
            return (isInteger(base) or isDecimal(base)) and isInteger(exponent)
        
        s = s.strip()  # Remove leading and trailing whitespace
        if not s:
            return False
        return isInteger(s) or isDecimal(s) or isExponent(s)
