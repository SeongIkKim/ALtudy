from collections import defaultdict

with open('inputs.txt') as f:
    rules, messages = f.read().strip().split('\n\n')
    rs = rules.strip().split('\n')
    messages = messages.strip().split('\n')

D = dict()
for r in rs:
    rhead, rbody = r.split(': ')
    rbody = rbody.replace('"','').split(' | ')
    if rbody[0].isalpha():
        D[rhead] = rbody[0]
    else:
        D[rhead] = [rule.split() for rule in rbody]


def match(string, stack):
    # 1개의 rule은 최소 1개이상 단어를 포함하므로, rule의 갯수가 string 길이보다 더 많을경우 체크할 필요 없음
    if len(stack) > len(string):
        return False
    # 예외처리 : 빈 문자열이 입력으로 들어올경우
    elif len(stack) == 0 or len(string) == 0:
        return len(stack) == 0 and len(string) == 0

    # 앞 rule부터 차례대로 수행
    # string의 head(첫글자)만 검사하고 다음 재귀함수로 넘기는 recursive가 포인트
    c = stack.pop()
    # 1. 재귀 끝에 도달했을때(문자를 찾음)
    if c.isalpha():
        # 가장 앞글자가 맞을경우
        if string[0] == c:
            # 다음 글자로 넘긴다. stack은 참조복사를 피해야한다.(참조 복사시 재귀 내 pop연산으로 stack이 깨진다)
            # 그렇지만 stack은 이중 리스트가 아니므로 얕은복사만 해서 넘겨도 된다.
            return match(string[1:], stack.copy())
    # 2. 재귀 도중(숫자 rule임)
    else:
        # 한 rule안에 갈래(|)가 있을 경우를 대비해 for문
        for rule in D[c]:
            # pop한 c 대신에 해당 rule을 추가하고, match 여부를 확인한다.
            if match(string, stack + list(rule[::-1])):
                return True
    return False


def valid_messages():
    total = 0
    for message in messages:
        if match(message, list(D['0'][0][::-1])): # message와 0의 rules 비교
            total += 1
    return total

D['8'] = [['42'],['42','8']]
D['11'] = [['42','31'],['42','11','31']]
print(valid_messages())


