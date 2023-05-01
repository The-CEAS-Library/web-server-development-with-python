def fib(n):
    if n < 0: return - 1
    f1 = 0
    f2 = 1

    if n == 0: return 0
    if n == 1: return 1

    for i in range(2, n + 1):

        new_f = f1 + f2

        f1 = f2
        f2 = new_f

    return f2

def compound_interest(principal, rate, tenure):
    return principal * (1 + rate ) ** (tenure)