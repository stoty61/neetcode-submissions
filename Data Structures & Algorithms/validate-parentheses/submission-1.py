class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        for char in s:
            print(char)
            if char == '(' or char == "{" or char == "[":
                stack.append(char)
                print("appended: ", char)
            
            elif char == ')':
                if len(stack) == 0:
                    return False
                recent = stack.pop()
                if recent != "(":
                    return False
                
            elif char == "}":
                if len(stack) == 0:
                    return False
                recent = stack.pop()
                if recent != "{":
                    return False
                
            elif char == "]":
                if len(stack) == 0:
                    return False
                recent = stack.pop()
                if recent != '[':
                    return False

        return len(stack) == 0
                

        