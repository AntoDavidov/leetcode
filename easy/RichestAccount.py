def maximum_wealth(accounts):
    richest_account = 0
    for account in accounts:
        if sum(account) >= richest_account:
            richest_account = sum(account)
    print(richest_account)

accs = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
maximum_wealth(accs)