import collections
import re
import string
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 1. translate로 punctuation 제거
        table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        # 2. lowercase 변환 후 공백으로 단어 분리
        words = paragraph.translate(table).lower().split()
        # 3. collections.Counter로 빈도 세고, 빈도 순으로 정렬
        counts = collections.Counter(words).most_common()

        for count in counts:  # ex) count - ('ball', 2)
            # count[0]가 단어, count[1]이 빈도수
            if count[0] in banned:
                continue
            return count[0]

'''
32ms(82.31%)
14.1MB(75.73%)
'''


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 1. re.sub(정규표현식 치환)으로 paragraph 내 word만 남기고 나머지 전부 공백으로 치환
        # 2. list comprehension에 조건식을 넣어 banned word는 가져오지 않도록 검사
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        counter = collections.Counter(words)

        return counter.most_common(1)[0][0]

'''
28ms(94.58%)
14MB(75.73%)
'''
