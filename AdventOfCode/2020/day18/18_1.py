with open('inputs.txt') as f :
    eps = f.read().strip().split('\n')

def cal(op,a,b):
    if op == '+':
        return a + b
    elif op == '*':
        return a * b
op = ['*','+']

values = []

for ep in eps:
    s = [letter for letter in ep.replace(' ', '')]
    stack = []
    for i in range(len(s)):

        if s[i].isdigit():
            s[i] = int(s[i])
            if stack and stack[-1] in op:
                stack.append(cal(stack.pop(),stack.pop(),s[i]))
            else:
                stack.append(s[i])

        elif s[i] == ')' :
            result = stack.pop()
            stack.pop() # '(' 제거
            while stack and stack[-1] in op:
                result = cal(stack.pop(),stack.pop(), result)
            stack.append(result)
        else:
            stack.append(s[i])
    if len(stack) != 1:
        raise Exception
    values.append(stack[-1])

print(values)
print(sum(values))




