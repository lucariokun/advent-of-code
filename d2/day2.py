value_dict = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

results_dict = {
    '0': 3,
    '-1': 6,
    '2': 6,
    '1': 0,
    '-2': 0
}

fixed_results = (
    (3, 1, 2),
    (4, 5, 6),
    (8, 9, 7)
)

total_score = int()
total_fixed_score = int()

with open('day2-input.txt', 'r') as input:
    for line in input:
        line.strip()
        p = value_dict[line[2]]
        e = value_dict[line[0]]
        match_result = results_dict[str(e-p)] + p
        total_score += match_result
        total_fixed_score += fixed_results[p-1][e-1]

print('Your total score would be: {}'.format(total_score))
print('Your total fixed score would be: {}'.format(total_fixed_score))