entirely_contained = int()
overlapping = int()

with open('d4/day4-input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        elves = line.split(',')
        for i, elf in enumerate(elves):
            elves[i] = elves[i].split('-')
        assignment_1 = set(range(int(elves[0][0]), int(elves[0][1])+1))
        assignment_2 = set(range(int(elves[1][0]), int(elves[1][1])+1))
        if assignment_1.issubset(assignment_2) or assignment_1.issuperset(assignment_2):
            entirely_contained += 1
        if assignment_1.intersection(assignment_2):
            overlapping += 1

    print('Entirely contained assignments: {}'.format(entirely_contained))
    print('Overlapping assignments: {}'.format(overlapping))