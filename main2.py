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


if __name__ == '__main__':
    tasks = {6: count_digits, 12: useless_symbols}
    print('Привет! У меня есть задачи:')
    for task_id, task_executor in tasks.items():
        print(f'{task_id}. {task_executor.__name__}')

    _id = input('Введи номер задачи: ')
    arg = input('Введи аргумент к задаче: ')

    r = tasks[int(_id)](arg)

    print(f'Результат выполнения:\n{r}')
