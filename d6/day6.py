buffer = list()

with open('day6-input.txt', 'r') as f:
    stream = f.readline()

for i, l in enumerate(stream):
    buffer.append(l)
    if len(buffer) > 4:
        buffer = buffer[-4:]
    if len(set(buffer)) == 4:
        print('First start-of-packet marker found at: {}'.format(i+1))
        break

for i, l in enumerate(stream):
    buffer.append(l)
    if len(buffer) > 14:
        buffer = buffer[-14:]
    if len(set(buffer)) == 14:
        print('First start-of-message marker found at: {}'.format(i+1))
        break