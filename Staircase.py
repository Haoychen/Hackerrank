__author__ = 'voelunteer'

def staircase(N):
    N = int(N)
    for i in range(N):
        j = i + 1
        print(" " * (N - j), end = "")
        print("#" * j)


staircase(input())