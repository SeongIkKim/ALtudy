with open('inputs.txt') as f:
    program = f.read().split('\n')[:-1]


acc = i = 0

# 프로그램 전체에서 명령어 하나하나씩 바꿔보기 위한 wrap 반복문
for change in range(len(program)):
    # 원래의 프로그램을 오염시키지 않고 지역변수 P라는 이름으로 새로 program을 할당
    P = list(program)
    if P[change][:3] == 'nop':
        P[change] = 'jmp ' +P[change].split()[1]
    elif P[change][:3] == 'jmp':
        P[change] = 'nop ' +P[change].split()[1]
    else:
        continue
    t = 0 # 몇번이나 수행되었는지
    i = 0 # 현재 수행하고 있는 operation index
    acc = 0
    while 0<=i<len(P) and t<1000: # 무한반복에 걸리지 않게 t<1000 조건을 걸어놓음
        t +=1
        op, arg = P[i].split()
        if op == 'acc':
            acc += int(arg)
            i += 1
        elif op == 'nop':
            i += 1
        elif op == 'jmp':
            i += int(arg)

    if i == len(P): # 성공적으로 프로그램을 종료했을 때 acc를 찍기
        print(acc)

'''
표본의 수가 작아 Brute Force로 푸는 풀이를 보고 참고했는데,
원래는 DFS, 백트래킹 문제라고.
느낌은 왔지만 코드를 몰라서...
추후에 다시 풀어보자.
'''
