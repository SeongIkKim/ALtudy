'''
def solution(heights):
    heights = [5,3,1,2,3]
    answer = [0]
    max = heights[0]
    max_index = 0
    for i in range(1,len(heights)):
        if heights[i]<heights[i-1]:
            # 1.뒷놈이 앞놈보다 작을 경우
            answer.append(i)
        elif heights[i]>heights[i-1]:
            # 2.뒷높이 앞놈보다 클 경우
            if max > heights[i]:
                # 2-1.뒷놈이 지금까지 max보다 작을 경우
                answer.append(max_index+1) # max_index는 인덱스이므로 n번째 수로 치환하여 append
            elif max < heights[i]:
                # 2-2.뒷놈이 지금까지 max보다 클 경우
                answer.append(0)
                max = heights[i]
                max_index = i
            else:
                # 2-3. 뒷놈과 max가 같을 경우
                answer.append(0)
                max = heights[i]
                max_index = i
        else:
            # 3.뒷놈과 앞놈이 같을경우
            if max > heights[i]:
                answer.append(max_index)
            else :
                answer.append(0)
                max = heights[i]
                max_index = i
    print(answer)
    return answer

이렇게 풀었다가 4번케이스가 틀렸다

이유는 stack을 제대로 구현안했기 때문.
[5,3,1,2,3]에서

2는 이전 놈인 1보다 크고 지금까지 max인 5보다 작지만, max인 수신탑이 받는게 아니라 5보다 작지만 더 가깝고 2보다 높은 탑인 3(index 1)이 받게된다.

'''


def solution(heights):
    # heights = [5,3,1,2,3]
    answer = [0]
    max = [(heights[0], 0)]  # max = [(높이,인덱스),....]
    for i in range(1, len(heights)):
        if heights[i] < heights[i - 1]:
            # 1.뒷놈이 앞놈보다 작을 경우
            answer.append(i)
            max.append((heights[i - 1], i - 1))
        elif heights[i] > heights[i - 1]:
            # 2.뒷높이 앞놈보다 클 경우
            if max[-1][0] > heights[i]:
                # 2-1.뒷놈이 지금까지 max보다 작을 경우
                answer.append(max[-1][1] + 1)  # max의 index는 인덱스이므로 n번째 수로 치환하여 append
            elif max[-1][0] < heights[i]:
                # 2-2.뒷놈이 지금까지 max보다 클 경우
                answer.append(0)
                max.append((heights[i], i))
            else:
                # 2-3. 뒷놈과 max가 같을 경우
                max.pop()

                while (max[-1][0] <= heights[i]):
                    max.pop()
                    if (max == []):
                        answer.append(0)
                        break;
                if (max):
                    answer.append(max[-1][1] + 1)
                max.append((heights[i], i))

        else:
            # 3.뒷놈과 앞놈이 같을경우
            if max[-1][0] > heights[i]:
                answer.append(max[-1][1] + 1)
            else:
                answer.append(0)
                max.append((heights[i], i))
    return answer


# 참고할만한 코드
def solution(heights):
    answer = [0] * len(heights)
    stack = []

    for i in reversed(range(len(heights))):
        while stack and stack[-1][1] < heights[i]:
            idx, height = stack.pop()
            answer[idx] = i + 1
        stack.append((i, heights[i]))

    return answer


if __name__ == '__main__':
    print(solution([5, 3, 1, 2, 3]))
'''
기본적인 아이디어는 비슷하지만, reverse 또는 range의 스텝 -1로 거꾸로 가면서 max를 검사하는것이 핵심.
그냥 쭉 따라가면서 다음 height보다 낮은 max를 pop해주고, 다시 갱신해주는 방식을 볼 것.
'''
