# Вариант 12

def not_prime_divs_sum(n: int):
    sm = 0
    logger = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            for div in [i, n // i]:
                count_divs = 0
                for j in range(1, int(div**0.5) + 1):
                    if div % j == 0:
                        count_divs += 2

                if count_divs > 2:
                    sm += div
                    logger.append(div)

    print(sm, logger)


def count_digits(n: int):
    count = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        if digit < 3:
            count += 1

    return count
