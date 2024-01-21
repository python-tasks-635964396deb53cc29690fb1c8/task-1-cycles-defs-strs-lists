STATE_NUM_OF_DAY = 0
STATE_MONTH = 1
STATE_NUM_OF_YEAR = 2
STATE_DAY_SPACE = 3
STATE_MONTH_SPACE = 4
STATE_OUT = 5
STATE_INTERRUPT = 6


def parse_dates(s: str) -> list[str]:
    dates = []
    state = STATE_INTERRUPT
    date_local = ''
    date = ''
    for char in (s + ' '):
        if (state == STATE_INTERRUPT or state == STATE_OUT or state == STATE_NUM_OF_DAY) and char.isdigit():
            state = STATE_NUM_OF_DAY
        elif state == STATE_NUM_OF_DAY and char.isspace():
            state = STATE_DAY_SPACE
        elif (state == STATE_DAY_SPACE or state == STATE_MONTH) and (not char.isspace()):
            state = STATE_MONTH
        elif state == STATE_MONTH and char.isspace():
            state = STATE_MONTH_SPACE
        elif (state == STATE_MONTH_SPACE or state == STATE_NUM_OF_YEAR) and char.isdigit():
            state = STATE_NUM_OF_YEAR
        elif state == STATE_NUM_OF_YEAR and (not char.isdigit()):
            state = STATE_OUT
        else:
            state = STATE_INTERRUPT

        date_local += char

        try:
            if state == STATE_OUT:
                if len(date_local) > 0 and date_local[0] == '0':
                    raise RuntimeError()
                date += date_local[:-1]
                dates.append(date)
            elif state == STATE_DAY_SPACE:
                if not (2 <= len(date_local) <= 3):
                    raise RuntimeError()
                date += date_local
                date_local = ''
            elif state == STATE_MONTH_SPACE:
                date += date_local
                date_local = ''
        except RuntimeError:
            state = STATE_INTERRUPT

        if state == STATE_OUT or state == STATE_INTERRUPT:
            date = ''
            date_local = ''

    return dates
