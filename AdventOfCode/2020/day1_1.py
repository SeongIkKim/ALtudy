with open('inputs.txt') as f:
    entries = enumerate(f.read().split('\n')[:-1])


entries_map = dict()

for i, entry in entries:
    if 2020 - int(entry) in entries_map:
        print(int(entry), 2020-int(entry), int(entry)*(2020-int(entry)))
    entries_map[int(entry)] = i
