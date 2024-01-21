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


def count_numbers_condition(n: int):
    count = 0

    sum_digits = 0
    local_n = n
    while local_n > 0:
        digit = local_n % 10
        local_n //= 10
        divs_count = 0
        for i in range(1, digit + 1):
            if digit % i == 0:
                divs_count += 1

        if divs_count <= 2:
            sum_digits += digit

    for i in range(1, n):
        if n % i != 0 and (not coprime_numbers(i, n)) and coprime_numbers(i, sum_digits):
            count += 1

    return count


def coprime_numbers(n: int, m: int) -> bool:
    for i in range(2, int(max(n, m)**0.5) + 1):
        if n % i == 0 and m % i == 0:
            return False

    return True
