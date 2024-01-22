def data_input(s: str = '') -> list[str]:
    data = []

    while 1:
        line = input()
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
