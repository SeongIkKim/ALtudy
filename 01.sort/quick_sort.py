def quick_sort(array):
    length = len(array)
    if length <= 1:
        return array

    less, equal, greater = [], [], []

    pivot = array[length//2]

    for i in array:
        if i > pivot:
            greater.append(i)
        elif i < pivot:
            less.append(i)
        else:
            equal.append(i)

    less = quick_sort(less)
    greater = quick_sort(greater)

    return less + equal + greater

'''
파이썬의 sort함수는 퀵정렬을 기본내장함수로 한다.
따라서 알고리즘의 원리만 파악하고 그냥 sort쓰자.

# 퀵정렬의 이점
정렬되지 않은 array에서 임의의 pivot을 뽑을경우 O(n log n)이라는 좋은 효율을 보여준다.

# 퀵정렬의 단점
이미(또는 거의)정렬된 상태의 array의 경우, 퀵 정렬이 훨씬 느리다.
정렬된 상태의 array는 삽입정렬을 사용하는것이 좋다.
'''
