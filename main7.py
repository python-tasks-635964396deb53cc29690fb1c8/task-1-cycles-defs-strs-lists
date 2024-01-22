def data_input(s: str = '') -> list[int]:
    data = []

    while 1:
        line = input(s)
        if not line:
            break
        data.append(int(line))

    return data


def reverse_min_max(numbers: list[int]) -> list[int]:
    mn, mx = min(numbers), max(numbers)
    m = list(map(lambda e: e[0], sorted([(numbers.index(mn), mn), (numbers.index(mx), mx)])))
    return numbers[:m[0]+1] + numbers[m[1]-1:m[0]:-1] + numbers[m[1]:]


def max_max(numbers: list[int]) -> list[int]:
    mx = max(numbers)
    numbers.remove(mx)
    return [mx, max(numbers)]


print(max_max(data_input()))
