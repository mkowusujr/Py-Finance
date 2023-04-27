import argparse


def setup_parser() -> argparse.ArgumentParser:
    # Setup Parser
    parser = argparse.ArgumentParser(
        prog='money-py',
        description='simple budget tracking in your terminal'
    )

    subparsers = parser.add_subparsers()

    # list COMMANDS

    parser_list = subparsers.add_parser('list')

    list_subparsers = parser_list.add_subparsers()

    parser_list_expenses = list_subparsers.add_parser('expenses')

    parser_list_expenses.add_argument(
        '-e', '-expense', type=str, dest='list_expenses_e')

    parser_list_expenses.add_argument(
        '-s', '-seller', type=str, dest='list_expenses_s')

    parser_list_expenses.add_argument(
        '-c', '-category', type=str, dest='list_expenses_c')

    parser_list_budgets = list_subparsers.add_parser('budgets')

    parser_list_budgets.add_argument(
        '-b', '-budget', type=str, dest='list_budgets_b')

    parser_list_incomes = list_subparsers.add_parser('incomes')

    parser_list_incomes.add_argument(
        '-i', '-incomes', type=str, dest='list_incomes_i')

    parser_list_reoccurring = list_subparsers.add_parser('reoccurring')

    parser_list_reoccurring.add_argument(
        '-s', '-search', type=str, default="", dest='list_reoccurring_s')

    parser_list_reoccurring.add_argument(
        '-e', '-expenses', action='store_true', dest='list_reoccurring_e')

    parser_list_reoccurring.add_argument(
        '-b', '-budgets', action='store_true', dest='list_reoccurring_b')

    parser_list_reoccurring.add_argument(
        '-i', '-incomes', action='store_true', dest='list_reoccurring_i')

    # BUDGET COMMANDS
    parser_budget = subparsers.add_parser('budget')

    parser_budget.add_argument(type=str,  nargs='?', dest='budget')

    parser_budget.add_argument(
        '-a', '-amount', type=float, nargs='?', dest='amount', required=True)

    parser_budget.add_argument(
        '-d', '-date', type=str, nargs='?', dest='date', required=True)

    parser_budget.add_argument(
        '-r', '-reoccurring', choices=['daily', 'weekly', 'bi-weekly', 'monthly', 'yearly'], default='0', dest='reoccurring')

    # EXPENSE COMMANDS
    parser_expense = subparsers.add_parser('expense')

    parser_expense.add_argument(type=str,  nargs='?', dest='expense')

    parser_expense.add_argument(
        '-s', '-seller', type=str, nargs='?', dest='seller', required=True)

    parser_expense.add_argument(
        '-a', '-amount', type=float, nargs='?', dest='amount', required=True)

    parser_expense.add_argument(
        '-d', '-date', type=str, nargs='?', dest='date', required=True)

    parser_expense.add_argument(
        '-c', '-category', type=str, nargs='?', dest='category', required=True)

    parser_expense.add_argument(
        '-r', '-reoccurring', choices=['daily', 'weekly', 'bi-weekly', 'monthly', 'yearly'], default='0', dest='reoccurring')

    # # Aggregate Cmds
    # parser.add_argument('--sum', action='store_true', dest='sum')

    # INCOME CMDS
    parser_income = subparsers.add_parser('income')

    parser_income.add_argument(type=str,  nargs='?', dest='income')

    parser_income.add_argument(
        '-a', '-amount', type=float, nargs='?', dest='amount', required=True)

    parser_income.add_argument(
        '-d', '-date', type=str, nargs='?', dest='date', required=True)

    parser_income.add_argument(
        '-r', '-reoccurring', choices=['daily', 'weekly', 'bi-weekly', 'monthly', 'yearly'], default='none', dest='reoccurring')
    return parser
