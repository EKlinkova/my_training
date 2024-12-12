numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

# Простое число — натуральное число, имеющее ровно два различных натуральных делителя. Другими словами,
# натуральное число p является простым, если оно отлично от 1 и делится без остатка только на 1 и на само p.

for n in numbers:
    is_prime = True # переменная простоты числа
    if n > 1:
        for i in range(2, n): # по определению простого числа, список > 1, т.е. с 2.
            if (n % 2) == 0:
                is_prime = False
                break
    else:
        is_prime = False
    if is_prime:
        primes.append(n)  # формируем список простых чисел
    else:
        not_primes.append(n) # формируем список сложных чисел
print(primes)
print(not_primes)