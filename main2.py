def count_digits(s: str) -> int:
    count = 0
    for char in s:
        if char.isdigit() and int(char) > 5:
            count += 1

    return count
