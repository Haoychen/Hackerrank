__author__ = 'voelunteer'

def plus_minus(T, Intergers):
    T = int(T)
    Input_list = Intergers.split()
    integer_list = []
    positive = 0
    negative = 0
    zero = 0
    for i in range(T):
        integer_list.append(int(Input_list[i]))
        if integer_list[i] > 0:
            positive += 1
        elif integer_list[i] < 0:
            negative += 1
        else:
            zero += 1
    print("%.3f" % (positive / T))
    print("%.3f" % (negative / T))
    print("%.3f" % (zero / T))

plus_minus(input(), input())



