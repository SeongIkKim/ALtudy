number_of_tc = int(input())

for i in range(number_of_tc):
    n, m = map(int, input().split())
    candies = sum(map(int, input().split()))
    q, r = divmod(candies, m)
    print(f"Case #{i+1}: {r}")
