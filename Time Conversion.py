__author__ = 'voelunteer'


def time_convert(Time):
    time_list = Time.split(':')
    if time_list[2][2] == "P":
        if time_list[0] != "12":
            time_list[0] = int(time_list[0])
            time_list[0] += 12
            time_list[0] = str(time_list[0])
    else:
        if time_list[0] == "12":
            time_list[0] = "00"
    print(time_list[0] + ":" + time_list[1] + ":" + time_list[2][:2])

time_convert(input())