import copy
stack = list()
duplicate_stack = list()

with open('day5-input.txt', 'r') as f:
    for line in f:
        if line.strip() and line.strip()[0] != '1' and line.strip()[0] != 'm':
            for i in range(int(len(line)/4)):
                if len(stack) <= i:
                    stack.append(list())
                cell = line[i*4:(i*4)+4]
                if cell.strip():
                    stack[i].append(cell.strip()[1])
        elif not line.strip():
            for l in stack:
                l.reverse()
            if not duplicate_stack:
                duplicate_stack = copy.deepcopy(stack)
        elif line.strip() and line.strip()[0] == 'm':
            line = line.split(' ')
            number_to_move = int(line[1])
            move_from = int(line[3])-1
            move_to = int(line[5])-1

            for i in range(number_to_move):
                stack[move_to].append(stack[move_from].pop())

            duplicate_stack[move_to] += duplicate_stack[move_from][-number_to_move:]
            del duplicate_stack[move_from][-number_to_move:]

print('Boxes on top of the stack: {}'.format(''.join([x[-1] for x in stack])))
print('Boxes on top of the stack, but moved in bulk: {}'.format(''.join([x[-1] for x in duplicate_stack])))