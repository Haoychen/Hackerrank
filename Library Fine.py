__author__ = 'voelunteer'

def library_fine(return_date, schedual_date):
    schedual_date_list = schedual_date.split()
    return_date_list = return_date.split()
    for i in range(3):
        schedual_date_list[i] = int(schedual_date_list[i])
        return_date_list[i] = int(return_date_list[i])
    if return_date_list[2] == schedual_date_list[2]:
        if return_date_list[1] == schedual_date_list[1]:
            if return_date_list[0] <= schedual_date_list[0]:
                return 0
            else:
                return 15 * (return_date_list[0] - schedual_date_list[0])
        elif return_date_list[1] < schedual_date_list[1]:
            return 0
        else:
            return_month = return_date_list[1]
            schedual_month = schedual_date_list[1]
            return 500 * (return_month - schedual_month)

    elif return_date_list[2] < schedual_date_list[2]:
        return 0
    else:
        return 10000

print(library_fine(input(), input()))