def divisors(number: int):
    if number ** 0.5 != int(number ** 0.5):  # если квадратный корень искомого числа - не натуральное число
        return False

    cnt = 0
    m = 0
    for i in range(2, int(number ** 0.5)):
        if number % i == 0:  # если делится на i
            if cnt == 0:
                cnt += 1
                m = i
            else:
                return False
    if m > 0:
        return number // m
    else:
        return False

for i in range(289123456,389123456+1):
    d = divisors(i)
    if d > 0:
        print(i, d)