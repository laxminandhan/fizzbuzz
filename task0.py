def fizz_buzz(n):
    return [(not n % 3) * 'Fizz' + (not n % 5) * 'Buzz' or n for n in range(1, 101)]
