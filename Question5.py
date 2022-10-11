class Solution:
    def isValid(self, s: str) -> bool:
        # For sure the number of brackets need to be an even Number - else we output false
        if len(s) % 2 != 0:
            return False
        dict = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for idx in s:
            if idx in dict.keys():
                stack.append(idx)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if idx!= dict[a]:
                    return False
        return stack == []
    
# User Input
s = "{[]}}"
print("The input is", s)
a = Solution()
Validity = a.isValid(s)
print("The given Input sequence is", Validity)
    

# The time complexity of the code is O(n).
