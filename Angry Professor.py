__author__ = 'voelunteer'


def angry_prof(limit, arrive_time):
    limit = limit.split()
    n = int(limit[0])
    k = int(limit[1])
    arrive_time = arrive_time.split()
    count = 0
    for i in range(n):
        arrive_time[i] = int(arrive_time[i])
        if arrive_time[i] <= 0:
            count += 1
    if count < k:
        print("YES")
    else:
        print("NO")


T = input()
T = int(T)
for i in range(T):
    angry_prof(input(), input())
