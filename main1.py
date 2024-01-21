# Вариант 12

from random import shuffle


def str_shuffle(s: str) -> str:
    words = list(map(lambda e: list(e.encode()), s.split()))
    for i in range(1, len(words) - 1):
        shuffle(words[i])

    words = list(map(lambda e: list(map(lambda el: chr(el), e)), words))
    return ' '.join(map(lambda e: ''.join(e), words))
