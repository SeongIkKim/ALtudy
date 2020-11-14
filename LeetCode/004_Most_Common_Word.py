import collections
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

