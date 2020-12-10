from collections import defaultdict

with open('inputs.txt') as f:
    ratings = [int(rating) for rating in  f.read().split('\n')[:-1]]

ratings.sort()
ratings.insert(0, 0)
ratings.append(ratings[-1]+3)

differences = defaultdict(int)

for i in range(len(ratings)-1):
    d = ratings[i+1]-ratings[i]
    differences[d] += 1

print(differences[1], differences[3])
print(differences[1] * differences[3])
