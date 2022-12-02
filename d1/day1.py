elf_calories = int()
calories = list()

with open('day1-input.txt', 'r') as f:
    for line in f:
        if line != '\n':
            elf_calories += int(line.strip('\n'))
        else:
            calories.append(elf_calories)
            elf_calories = 0

calories.sort(reverse=True)
print('Calories carried by the elf with the most calories: {}'.format(calories[0]))

top_three_calories = int()
for c in calories[0:3]:
    top_three_calories += c
print('The three elves with the most calories have a total combined of: {}'.format(top_three_calories))