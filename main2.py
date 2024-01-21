def count_digits(s: str) -> int:
    count = 0
    for char in s:
        if char.isdigit() and int(char) > 5:
            count += 1

    return count


def useless_symbols(s: str) -> str:
    useless = ''
    ru_seq = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    seq = set(map(lambda e: e.lower(), s))
    for ru_char in ru_seq:
        useless += ru_char if ru_char not in seq else ''

    return useless
