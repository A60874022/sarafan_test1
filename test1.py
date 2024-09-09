n = int(input())


def sequence_calculation(n):
    """Функция вывода n первых 
    элементов последовательности 122333444455555… 
    (число повторяется столько раз, чему оно равно."""
    temp = []
    i = 1
    while len(temp) < n:
        number = [i] * i
        temp.extend(number)
        i += 1
    sequence = [str(number) for number in temp][:n]
    return ''.join(sequence)


print(sequence_calculation(n))