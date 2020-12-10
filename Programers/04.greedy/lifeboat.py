'''
1. boat 개수를 최대한 넉넉하게 잡는다(모두 혼자탄다고 가정)
2. 사람들을 무게순으로 줄세운다 (sort)
3. 가장 무거운 사람과 가장 가벼운 사람을 합쳐서
    3-1. limit를 넘으면 무거운 사람은 혼자타도록 pop한다
    3-2. limit를 넘지 않으면 두명을 세트지어서 한 대로 내보내고 구명보트 1대를 절약한다
'''

from collections import deque

def solution(people, limit):
    boat = len(people) # 최악의 상황으로 boat를 모두 혼자 타야된다고 가정한다(모두들 무거워서 어떤 조합으로도 2명이서 탈 수 없다)
    people.sort() #무게 순으로 정렬한다.
    people= deque(people)
    
    # 최후에 탈출하는 인원이 1명이면 len(people) == 1 (마지막 한 사람이 탈출하기 직전)
    # 최후에 탈출하는 인원이 2명이면 len(peple) == 0 (마지막 두 사람이 탈출하고 난 후)
    while len(people)>1:
        # 가장 가벼운 사람과 가장 무거운 사람을 같이 태우려 했을때 못탄다면
        # 가장 무거운 사람은 혼자 타야한다는 소리이다. (혼자 타도록 pop)
        if people[0] + people[-1] > limit: 
            people.pop()
        # 가장 가벼운 사람과 가장 무거운 사람을 같이 태우려 했을때 탈수 있다면
        # 그대로 두 명을 짝지어 내보내는게 가장 효율성이 좋다. (둘다 pop하고, 구명보트 1개를 절약)
        else :
            people.popleft()
            people.pop()
            boat-=1
    
    return boat