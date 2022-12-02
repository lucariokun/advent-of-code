value_dict = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}

# Matrixes represent the score from the outcome for the match.
# The second letter in the line of the input file always
# represents the X coordinate, while the first represents the Y.
#
# In both matrixes Y represents what the elf will play.
# In the first matrix X represents what you will play,
# while in the second matrix it represents what outcome the match will have. 

p1_matrix = (
    (4, 1, 7),
    (8, 5, 2),
    (3, 9, 6)
)

p2_matrix = (
    (3, 1, 2),
    (4, 5, 6),
    (8, 9, 7)
)

p1_score = int()
p2_score = int()

with open('day2-input.txt', 'r') as input:
    for line in input:
        line.strip()
        _x = value_dict[line[2]]
        _y = value_dict[line[0]]
        p1_score += p1_matrix[_x][_y]
        p2_score += p2_matrix[_x][_y]

print('Part 1 score: {}'.format(p1_score))
print('Part 2 score: {}'.format(p2_score))