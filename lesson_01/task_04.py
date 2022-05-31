import numpy


def deposit(total, duration):
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
                        result += procents[total_count][cur_duration] * 0.01 * result / 12
                    return result


total = float(input('Введите сумму депозита, руб.'))
duration = int(input('Введите продолжительность, мес.'))

print(deposit(total, duration))
