def data_input(s: str = '') -> list[str]:
    data = []

    while 1:
        line = input(s)
        if not line:
            break
        data.append(line)

    return data


def sort_by_frequency(s: list[str]) -> list[str]:
    alphabet = {}
    s_frequency = []
    for line in s:
        local_alphabet = {}
        for char in line:
            local_alphabet[char] = local_alphabet[char] + 1 if char in local_alphabet else 1
            alphabet[char] = alphabet[char] + 1 if char in alphabet else 1

        symbol, count = sorted(local_alphabet.items(), key=lambda e: e[1])[-1]
        s_frequency.append((symbol, count, line))

    return list(map(lambda el: el[2], sorted(s_frequency, key=lambda e: e[1] - alphabet[symbol])))


def sort_by_middle(s: list[str]) -> list[str]:
    # 6 В порядке увеличения медианного значения выборки строк (прошлое
    # медианное значение удаляется из выборки и производится поиск нового
    # медианного значения).

    # медианного значения чего? Длины? Высоты? Ширины? Какой выборки? Случайной? Выборка на основании чего?
    pass


def sort_by_ascii_code(s: list[str]) -> list[str]:
    data = []
    for line in s:
        max_letter = ord(max(line))
        values = []
        for i in range(len(line) // 2):
            values.append(abs(ord(line[i]) - ord(line[len(line) - 1])))
        values = list(map(lambda e: (max_letter - e)**2, values))
        data.append((line, (sum(values) / len(values))**0.5))

    return list(map(lambda el: el[0], sorted(data, key=lambda e: e[1])))


def sort_by_palindrome_count(s: list[str]) -> list[str]:
    data = []
    for line in s:
        count = 0
        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                count += 1
        data.append((line, count**2 / count if count != 0 else count))

    return list(map(lambda el: el[0], sorted(data, key=lambda e: e[1])))


if __name__ == '__main__':
    tasks = {3: sort_by_frequency, 6: sort_by_middle, 9: sort_by_ascii_code, 10: sort_by_palindrome_count}
    print('Привет! У меня есть задачи:')
    for task_id, task_executor in tasks.items():
        print(f'{task_id}. {task_executor.__name__}')

    _id = input('Введи номер задачи: ')
    arg = data_input('Введи аргумент к задаче: ')

    r = tasks[int(_id)](arg)

    print(f'Результат выполнения:\n{r}')
