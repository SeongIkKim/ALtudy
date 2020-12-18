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
                if stack[-1] == '+':
                    stack.append(cal(stack.pop(),stack.pop(),s[i]))
                else : # '*'
                    stack.append(s[i])
            else: # 수식의 앞 숫자
                stack.append(s[i])

        elif s[i] == ')' :
            result = stack.pop()
            while stack and stack[-1] in op:
                result = cal(stack.pop(),stack.pop(), result)
            stack.pop() # '( 제거
            # 앞에 남은 '+' 다 처리('*'와 순서가 섞이지 않게)
            while stack and stack[-1] == '+':
                result = cal(stack.pop(),stack.pop(), result)
            stack.append(result)
        else:
            stack.append(s[i])
    if len(stack) != 1:
        a = []
        result = stack.pop()
        while stack and stack[-1] in op:
            result = cal(stack.pop(),stack.pop(),result)
        stack.append(result)
    values.append(stack[-1])

print(values)
print(sum(values))




