# Вариант 12

from random import shuffle


def str_shuffle(s: str) -> str:
    words = list(map(lambda e: list(e.encode()), s.split()))
    for i in range(1, len(words) - 1):
        shuffle(words[i])

    words = list(map(lambda e: list(map(lambda el: chr(el), e)), words))
    return ' '.join(map(lambda e: ''.join(e), words))


def sort_chars_digits(s: str) -> str:
    return ''.join(sorted(s))


if __name__ == '__main__':
    tasks = {6: str_shuffle, 12: sort_chars_digits}
    print('Привет! У меня есть задачи:')
    for task_id, task_executor in tasks.items():
        print(f'{task_id}. {task_executor.__name__}')

    _id = input('Введи номер задачи: ')
    arg = input('Введи аргумент к задаче: ')

    r = tasks[int(_id)](arg)

    print(f'Результат выполнения:\n{r}')
