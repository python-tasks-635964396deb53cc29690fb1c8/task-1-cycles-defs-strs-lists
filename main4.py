data = []

while 1:
    line = input()
    if not line:
        break
    data.append(line)

print('\n'.join(sorted(data, key=len)))
