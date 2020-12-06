from typing import List
import re

# 1st try

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = {}
        digit_logs = []
        for i in range(len(logs)):
            identifier, content = logs[i].split(sep=" ", maxsplit=1)
            if re.match('^\d.*', content):  # 숫자로 시작하면 (digit-logs)
                digit_logs.append(logs[i])
            else: # 영문자로 시작하면 dictionary로 바꿈
                letter_logs[identifier] = content

        # 딕셔너리 정렬 - 기준 1 : log-content, 기준 2 : identifier
        logs = [' '.join([k, v]) for k, v in sorted(letter_logs.items(), key=lambda item: (item[1], item[0]))]

        logs.extend(digit_logs)

        return logs

'''
테스트케이스 실패
'''


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []

        for log in logs:
            if log.split()[1].isdigit():  # 숫자 log
                digits.append(log)
            else:  # 문자 log
                letters.append(log)

        # lambda sorting 사용법을 익힐것.
        # x는 매개변수를 나타내는데, 여기서는 letters의 element이다
        # 첫 번째 기준으로 content, 두 번째 기준으로 identifier를 잡고 있다
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits

'''
36ms(67.88%)
14.2MB(64.99%)

1. lambda sorting
2. isdigit, isalpha, isalnum같은 판별함수의 사용을 잘 하자
3. split함수의 유연한 사용
'''
