priority_values = dict()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet += alphabet.upper()

for i, l in enumerate(alphabet):
    priority_values[l] = i+1

total_priority = int()
badges_priority = int()

groups = list()

raw_input = list()

with open('day3-input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        raw_input.append(line)
        compartments = [
            line[0:int((len(line)/2))],
            line[int((len(line)/2)):]
            ]
        common_item = next(iter(set(compartments[0]).intersection(compartments[1])))
        priority = priority_values[common_item]
        total_priority += priority

n_groups = int(len(raw_input)/3)
for i in range(n_groups):
    group = list()
    for j in range(3):
        group.append(raw_input.pop(0))
    groups.append(group)

for group in groups:
    badge = next(iter(set(group[0]).intersection(group[1], group[2])))
    priority = priority_values[badge]
    badges_priority += priority

print('Total priority for shared items in compartments: {}'.format(total_priority))
print('Total priority for badges: {}'.format(badges_priority))