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
    return numbers[:m[0] + 1] + numbers[m[1] - 1:m[0]:-1] + numbers[m[1]:]


def max_max(numbers: list[int]) -> list[int]:
    mx = max(numbers)
    numbers.remove(mx)
    return [mx, max(numbers)]


def max_odd(numbers: list[int]) -> int:
    while len(numbers) > 0:
        mx = max(numbers)
        if mx % 2 != 0:
            return mx
        else:
            numbers.remove(mx)


def frequency_seq(numbers: list[int]) -> list[int]:
    return [max(set(numbers), key=numbers.count) for _ in numbers]


def list_div_index(numbers: list[int]) -> list[int]:
    return [numbers[i] for i in range(len(numbers)) if i != 0 and numbers[i] % i == 0 and
            numbers.count(numbers[i]) == 1]


if __name__ == '__main__':
    tasks = {12: reverse_min_max, 24: max_max, 36: max_odd, 48: frequency_seq, 60: list_div_index}
    print('Привет! У меня есть задачи:')
    for task_id, task_executor in tasks.items():
        print(f'{task_id}. {task_executor.__name__}')

    _id = input('Введи номер задачи: ')
    arg = data_input('Введи аргумент к задаче: ')

    r = tasks[int(_id)](arg)

    print(f'Результат выполнения:\n{r}')
