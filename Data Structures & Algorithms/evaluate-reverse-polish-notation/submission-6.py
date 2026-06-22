class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ("+", "-", "/", "*")
        for token in tokens:
            print(stack)
            if token not in operators:
                stack.append(int(token))
                continue
            one = stack.pop()
            two = stack.pop()
            if token == "+":
                ans = one + two
                stack.append(ans)
            elif token == "-":
                ans = two - one
                stack.append(ans)
            elif token == "*":
                ans = one * two
                stack.append(ans)
            elif token == "/":
                ans = int(two / one)
                stack.append(ans)

        
        return stack[0]
            


                