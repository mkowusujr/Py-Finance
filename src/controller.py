import repo


def handle_args(options):
    if options.record is True:
        repo.add_expense(options.expense, options.seller,
                         options.amount, options.date, options.category)
    elif options.budget is not None:
        repo.add_budget_category(
            options.budget, options.date, options.amount)
    elif options.display == 'entries':
        e = options.expense
        s = options.seller
        c = options.category

        expenses = repo.select_expenses(
            e if e is not None else "", s if s is not None else "", c if c is not None else "")
        print(expenses)

        if options.sum is True:
            total = sum(float(expense[2]) for expense in expenses)
            print(f'Total: ${total}')
