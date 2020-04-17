def quick_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr

    less, equal, greater = [], [], []
    pivot = arr[length // 2]

    for i in arr:
        if i > pivot:
            greater.append(i)
        elif i < pivot:
            less.append(i)
        else:
            equal.append(i)

    less = quick_sort(less)
    greater = quick_sort(greater)

    return greater + equal + less


def int_to_float(arr):
    f_arr = []
    for i in arr:
        i = float(i)
        while (i > 9):
            i /= 10
        f_arr.append(i)

    print("int_to_float")
    print(f_arr)

    return f_arr


def float_to_int(arr):
    i_arr = []
    for i in arr:
        str_i = str(i)
        length = len(str_i)
        if length == 3:
            pass  # 한자릿수
        elif length == 4:
            i = i * 10  # 두자릿수
        elif length == 5:
            i = i * 100  # 세자릿수
        elif length == 6:
            i = i * 1000  # 네자릿수
        else:
            print("wrong")

        i_arr.append(int(i))

    print("float_to_int")
    print(i_arr)

    return i_arr


def classfication(arr):
    d1 = []
    d2 = []
    d3 = []
    d4 = []

    s_arr = quick_sort(arr)

    while 1:
        break
    # index찾아내서 잘라내기

    # 잘라낸 d1,d2,d3,d4합치기

    return #합친문자열반환


def solution(numbers):
    filtered_nums = classfication(numbers)
    print(filtered_nums)

    # f_numbers = int_to_float(numbers)
    # sorted_f_numbers = quick_sort(f_numbers)
    # print("sorted_f_numbers")
    # print(sorted_f_numbers)
    # i_numbers = float_to_int(sorted_f_numbers)

    answer = ''
    return answer
