__author__ = 'voelunteer'


def factorial(n):
    i = 1
    factorial = 1
    while i <= n:
        factorial *= i
        i += 1
    return factorial

n = input()
n = int(n)
print(factorial(n))