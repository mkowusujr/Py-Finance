import repo
import pandas as pd
from tabulate import tabulate


def handle_args(options):
    if 'expense' in vars(options):
        budget, spent, remaining = repo.add_expense(options.expense, options.seller,
                                                    options.amount, options.date, options.category, options.reoccurring)

        print(
            f'Added Successfully\n{options.category} Budget: {budget:.2f}\nSpent: ${spent:.2f}\nRemaing {options.category} Budget: ${remaining:.2f}')
    if 'budget' in vars(options):
        repo.add_budget(
            options.budget, options.date, options.amount, options.reoccurring)
    if 'income' in vars(options):
        repo.add_income(options.income, options.amount,
                        options.date, options.reoccurring)
    if 'list_expenses_e' in vars(options):
        e = options.list_expenses_e
        s = options.list_expenses_s
        c = options.list_expenses_c

        expenses = repo.select_expenses(
            e if e is not None else "", s if s is not None else "", c if c is not None else "")
        expenses_df = pd.DataFrame(expenses, columns=[
            'Expense ID', 'Expense Name', 'Seller', 'Price', 'Purchase Date', 'Budget', 'Reoccurring']).set_index('Expense ID')

        print(tabulate(expenses_df, headers='keys', tablefmt='psql'))

        sum = expenses_df['Price'].apply(lambda p: float(p)).sum()
        avg = expenses_df['Price'].apply(lambda p: float(p)).mean()
        mode = expenses_df['Expense Name'].mode().tolist()
        print(f"\nsum: ${sum:.2f}\navg: ${avg:.2f}\nmode: {mode}")
    if 'list_budgets_b' in vars(options):
        b = options.list_budgets_b

        budgets = repo.select_budgets(b if b is not None else "")
        budgets_df = pd.DataFrame(budgets, columns=[
            'Budget ID', 'Budget Name', 'Budget Amount', 'Budget Date', 'Reoccurring']).set_index('Budget ID')
        print(tabulate(budgets_df, headers='keys', tablefmt='psql'))
    if 'list_incomes_i' in vars(options):
        i = options.list_incomes_i

        incomes = repo.select_incomes(i if i is not None else "")
        incomes_df = pd.DataFrame(incomes, columns=[
            'Income ID', 'Income Name', 'Income Amount', 'Income Date', 'Reoccurring']).set_index('Income ID')
        print(tabulate(incomes_df, headers='keys', tablefmt='psql'))
    if 'list_reoccurring_e' in vars(options):
        s = options.list_reoccurring_s
        e = options.list_reoccurring_e
        b = options.list_reoccurring_b
        i = options.list_reoccurring_i

        if e is False and b is False and i is False:
            e = b = i = True

        reoccurring = repo.select_reoccurring(s, e, b, i)
        if e:
            reoccurring_expenses_df = pd.DataFrame(reoccurring[0], columns=[
                'Expense ID', 'Expense Name', 'Seller', 'Price', 'Purchase Date', 'Budget', 'Reoccurring']).set_index('Expense ID')
            print(tabulate(reoccurring_expenses_df,
                  headers='keys', tablefmt='psql'))
            print('\n\n')

        if b:
            reoccurring_budgets_df = pd.DataFrame(reoccurring[1], columns=[
                'Budget ID', 'Budget Name', 'Budget Amount', 'Budget Date', 'Reoccurring']).set_index('Budget ID')
            print(tabulate(reoccurring_budgets_df,
                  headers='keys', tablefmt='psql'))
            print('\n\n')

        if i:
            reoccurring_incomes_df = pd.DataFrame(reoccurring[2], columns=[
                'Income ID', 'Income Name', 'Income Amount', 'Income Date', 'Reoccurring']).set_index('Income ID')
            print(tabulate(reoccurring_incomes_df,
                  headers='keys', tablefmt='psql'))
    if 'update_budget_id' in vars(options):
        pass
    if 'update_expense_id' in vars(options):
        pass
    if 'update_income_id' in vars(options):
        pass
    if 'delete_budget_id' in vars(options):
        repo.delete_budget(options.delete_budget_id)
    if 'delete_expense_id' in vars(options):
        repo.delete_expense(options.delete_expense_id)
    if 'delete_income_id' in vars(options):
        repo.delete_income(options.delete_income_id)


def handle_reoccurring_events():
    expenses, budgets, incomes = repo.select_reoccurring(
        search_term="", show_b=True, show_e=True, show_i=True)
    pass
