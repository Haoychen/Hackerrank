__author__ = 'voelunteer'


def utopian_tree(num_circle):
    num_circle = int(num_circle)
    height = 1
    if num_circle == 0:
        return 1
    i = 1
    while i <= num_circle:
        if i % 2 == 1:
            height *= 2
        else:
            height += 1
        i += 1
    return height

T = input()
T = int(T)
for i in range(T):
    print(utopian_tree(input()))

