__author__ = 'voelunteer'

def simple_array_sum(num_of_integers, integers):
    integer_list = integers.split()
    for i in range(int(num_of_integers)):
        integer_list[i] = int(integer_list[i])
    return sum(integer_list)

print(simple_array_sum(input(), input()))
