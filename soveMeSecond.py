__author__ = 'voelunteer'


T = int(input())
input_line = []
input_list = []
result = []
for i in range(T):
    input_line[i] = input()
    input_list[i] = input_line[i].split()
    A = int(input_list[i][0])
    B = int(input_list[i][1])
    result[i] = A + B
for i in range(T):
    print(result[i])
