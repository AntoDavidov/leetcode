def difference_of_sum(n, m):
    list_of_numbers_not_div_by_m = []
    list_of_numbers_div_by_m = []
    for i in range(1, n + 1):
        if i % m == 0:
            list_of_numbers_div_by_m.append(i)
        else:
            list_of_numbers_not_div_by_m.append(i)

    print(sum(list_of_numbers_not_div_by_m) - sum(list_of_numbers_div_by_m))


n1 = 5
m1 = 1
difference_of_sum(n1, m1)
