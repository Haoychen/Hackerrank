__author__ = 'voelunteer'


def largest_decent_num(n):
    n = int(n)
    reminder = n % 3
    num_of_5 = int(n / 3) * 3
    while num_of_5 >= 0:
        if reminder % 5 == 0:
            num_of_3 = reminder
            print("5" * num_of_5, end = "")
            print("3" * num_of_3)
            return
        else:
            num_of_5 -= 3
            reminder += 3
    print("-1")


T = input()
T = int(T)
for i in range(T):
    largest_decent_num(input())