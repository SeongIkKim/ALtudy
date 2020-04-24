def solution(l, w, tw):
    answer = 0
    before = tw
    cross = []
    cross_timer = []
    after = []
    
    sum_w = 0
    
    i=0
    while before or cross:
        if cross_timer and cross_timer[0]+l == i:
            # 다리를 다 건넌 트럭을 처리
            fin_t = cross.pop(0)
            cross_timer.pop(0)
            sum_w -= fin_t
            after.append(fin_t)
        # 다리에 더 들어올 수 있는 놈이 있으면 진입시킨다
        if before and sum_w+before[0] <=w:
            start_t = before.pop(0)
            cross.append(start_t)
            cross_timer.append(i)
            sum_w += start_t
        
        # print("after",after,"cross",cross,"before",before)
        i+=1

    return i
