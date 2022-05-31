import numpy


def deposit(total, duration, extra=0):
    procents = {
        10_000: {12: 5, 24: 6, numpy.inf: 5, },
        100_000: {12: 6, 24: 7, numpy.inf: 6.5, },
        1_000_000: {12: 7, 24: 8, numpy.inf: 7.5, }
    }

    if total < 1000 or duration < 6:
        result = 'Неверные данные'
        return result

    for total_count, cur_procents in procents.items():
        if total <= total_count:
            for cur_duration in cur_procents:
                if duration < cur_duration:
                    result = total
                    for i in range(duration):
                        if 1 < i < duration - 1:
                            result += extra
                        result += procents[total_count][cur_duration] * 0.01 * result / 12

                    return result


total = float(input('Введите сумму депозита, руб.'))
duration = int(input('Введите продолжительность, мес.'))
extra = int(input('Введите ежемесячный платеж, руб.'))

print(deposit(total, duration, extra))
