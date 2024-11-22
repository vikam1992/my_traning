
def is_prime(func):
    def printer(*args):
        counter = 0
        result = func(*args)
        for i in range(2, int(result**0.5) + 1):
            if result % i == 0:
                counter += 1
        if counter <= 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return printer

@is_prime
def sum_three(a, b, c):
    summa = a + b + c
    return summa

result = sum_three(2, 3, 6)
print(result)
