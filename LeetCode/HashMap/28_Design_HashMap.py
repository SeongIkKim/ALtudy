import collections


class ListNode:

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.map = collections.defaultdict(ListNode)  # separate chaning 사용

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size  # 간단한 modulo 방식으로 해싱
        if self.map[index].val is None:
            self.map[index] = ListNode(key, value)
            return
        p = self.map[index]
        while p:
            # 종료 조건 1
            # 해당 키가 존재할 경우, 업데이트하고 탈출
            if p.key == key:
                p.val = value
                return
            # 종료 조건 2
            # 체인의 마지막에 도달했을 경우
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)
        return

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        if self.map[index].val is None:
            return -1
        p = self.map[index]
        while p:
            if p.key == key:
                return p.val
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        if self.map[index].val is None:
            return -1
        p = self.map[index]
        if p.key == key:
            self.map[index] = ListNode() if p.next == None else p.next
            return
        while p.next:
            if p.next.key == key:
                p.next = p.next.next
                return
            p = p.next
        return -1

'''
기본적인 해쉬맵 구현
1. 해싱 키를 구하는 방식으로 모듈로를 사용했음. (key % size)
2. open addressing이 아닌 separate chaning 방식을 사용했음.
3. defaultdict를 사용하여 ListNode의 조회에 에러가 뜨는 경우가 없도록 하였음.
separate chaning의 경우, 같은 키에 연결리스트를 사용해 추가로 달아두므로,
해쉬 테이블의 크기(size)를 넘어서도 저장이 가능하다. 그러나 최악의 경우 탐색 시간이 O(n).
open addressing의 경우, 해당 키에 값이 존재하면, 다음 인덱스로 넘어가서 저장한다.
따라서 탐색시간은 비교적 짧아지지만, 클러스터링의 위험성이 있고, 로드팩터가 0.8이 넘어갈 경우 효율이 급격히 안좋아진다.
'''
