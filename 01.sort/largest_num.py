'''
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
        while (i > 9):
            i = float(i)
            i /= 10
        f_arr.append(i)

    # print("int_to_float")
    # print(f_arr)

    return f_arr


def float_to_int(arr):
    i_arr = []
    for i in arr:
        str_i = str(i)
        length = len(str_i)
        if length == 1: pass # 한자릿수
        elif length == 3: i = i * 10 # 두자릿수
        elif length == 4: i = i * 100 # 세자릿수
        elif length == 5: i = i * 1000 # 네자릿수
        else:
            print("wrong")
        
        i_arr.append(int(i))
        
    # print("float_to_int")
    # print(i_arr)

    return i_arr


def solution(numbers):
    
    f_numbers = int_to_float(numbers)
    sorted_f_numbers = quick_sort(f_numbers)
    # print("sorted_f_numbers")
    # print(sorted_f_numbers)
    i_numbers = float_to_int(sorted_f_numbers)
    
    answer = ''
    
    for i in i_numbers:
        str_i = str(i)
        answer += str_i
    
    print(answer)
    return answer

이게 첫 코드였으나 시간복잡도 초과로 실패.
'''

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x:x*4, reverse=True) # 문자열도 정렬된다. 사전식 정렬(가나다순 같은 느낌).
    # key를 x*4이상으로 잡아야하는 이유는 numbers의 원소가 최대 네자릿수이기 때문이다.(최소 4자리수로 만들어주고 비교해준다)
    # key를 x*3으로 잡아도 된다는데 네자릿수가 1000밖에 없어서 그런가?


    # 기억해야할 포인트
    # 1. 주어진 리스트의 길이가 10만 이상일경우 for문을 한번만 돌아야한다.(그래야 1초가량이 걸려서 시간복잡도를 통과한다)
    # 2. sort함수는 문자열을 사전식으로 정렬한다.
    # 3. sort함수를 실행할 때 lambda로 key를 지정해줄 수 있다(이경우 새 변수의 할당이 필요없다)
    # 4. str->int->str으로 바꾸어 0을 제거하는 사용법 - ['0','0','0','0'] 같은 예외케이스에 대하여

    return str(int(''.join(numbers)))
