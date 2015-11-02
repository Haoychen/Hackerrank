__author__ = 'voelunteer'

def diagonal_difference(n):
    n = int(n)
    matrix_list = []
    for i in range(n):
        matrix_list.append(input().split())
        for j in range(n):
            matrix_list[i][j] = int(matrix_list[i][j])
    main_diagonal = 0
    anti_diagonal = 0
    k = 0
    while k <= n - 1:
        main_diagonal += matrix_list[k][k]
        anti_diagonal += matrix_list[k][n - 1 - k]
        k += 1
    return abs(main_diagonal - anti_diagonal)

print(diagonal_difference(input()))

