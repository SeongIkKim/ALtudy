with open('inputs.txt') as f:
    ratings = [int(rating) for rating in  f.read().split('\n')[:-1]]

ratings.append(0)
ratings.sort()
ratings.append(ratings[-1]+3)

DP = {}
# dp(i) = 현재 ratings[i]에서 출발해서 마지막까지 도착하는 complete chain의 갯수
def dp(i):
    if i == len(ratings)-1:
        # 끝을 찍으면, complete chaine이므로 1을 돌려준다(누적 1 추가)
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i+1, len(ratings)):
        if ratings[j] - ratings[i] <= 3:
            # dp 재귀 호출
            ans += dp(j)
        else:
            break
    DP[i] = ans # 해당 노드에서 출발하는 complet chain의 갯수를 메모이제이션
    return ans

print(dp(0))

# dfs가 아니고 dp 문제였다!!!
# dfs로도 시간복잡도가 딸린다.. trillion

# https://www.youtube.com/watch?v=cE88K2kFZn0&ab_channel=JonathanPaulson
