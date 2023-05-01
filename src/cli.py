import argparse


def setup_parser() -> argparse.ArgumentParser:
    # Setup Parser
    parser = argparse.ArgumentParser(
        prog='money-py',
        description='simple budget tracking in your terminal'
    )

    subparsers = parser.add_subparsers()

    # list COMMANDS
    setup_list_cmds(subparsers)

    # UPDATE COMMANDS
    setup_update_cmds(subparsers)

    # BUDGET COMMANDS
    setup_budget_cmds(subparsers)

    # EXPENSE COMMANDS
    setup_expense_cmd(subparsers)

    # INCOME CMDS
    setup_income_cmds(subparsers)

    return parser


def setup_list_cmds(subparsers):
    def setup_list_expenses(list_subparsers):
        parser_list_expenses = list_subparsers.add_parser('expenses')

        parser_list_expenses.add_argument(
            '-e', '-expense', type=str, dest='list_expenses_e')

        parser_list_expenses.add_argument(
            '-s', '-seller', type=str, dest='list_expenses_s')

        parser_list_expenses.add_argument(
            '-c', '-category', type=str, dest='list_expenses_c')

    def setup_list_budgets(list_subparsers):
        parser_list_budgets = list_subparsers.add_parser('budgets')

        parser_list_budgets.add_argument(
            '-b', '-budget', type=str, dest='list_budgets_b')

        parser_list_incomes = list_subparsers.add_parser('incomes')

        parser_list_incomes.add_argument(
            '-i', '-incomes', type=str, dest='list_incomes_i')

    def setup_list_reoccurring(list_subparsers):
        parser_list_reoccurring = list_subparsers.add_parser('reoccurring')

        parser_list_reoccurring.add_argument(
            '-s', '-search', type=str, default="", dest='list_reoccurring_s')

        parser_list_reoccurring.add_argument(
            '-e', '-expenses', action='store_true', dest='list_reoccurring_e')

        parser_list_reoccurring.add_argument(
            '-b', '-budgets', action='store_true', dest='list_reoccurring_b')

        parser_list_reoccurring.add_argument(
            '-i', '-incomes', action='store_true', dest='list_reoccurring_i')

    parser_list = subparsers.add_parser('list')
    list_subparsers = parser_list.add_subparsers()
    setup_list_expenses(list_subparsers)
    setup_list_budgets(list_subparsers)
    setup_list_reoccurring(list_subparsers)


def setup_update_cmds(subparsers):
    def setup_update_expense(update_subparsers):
        parser_update_expenses = update_subparsers.add_parser('expense')

        parser_update_expenses.add_argument(type=int, dest="update_expense_id")

    def setup_update_budget(update_subparsers):
        pass

    def setup_update_income(update_subparsers):
        pass

    def setup_update_reoccurring(update_subparsers):
        pass

    parser_update = subparsers.add_parser('update')
    update_subparsers = parser_update.add_subparsers()
    setup_update_expense(update_subparsers)


def setup_delete_cmds(subparsers):
    pass


def setup_budget_cmds(subparsers):
    parser_budget = subparsers.add_parser('budget')

    parser_budget.add_argument(type=str,  nargs='?', dest='budget')

    parser_budget.add_argument(
        '-a', '-amount', type=float, nargs='?', dest='amount', required=True)

    parser_budget.add_argument(
        '-d', '-date', type=str, nargs='?', dest='date', required=True)

    parser_budget.add_argument(
        '-r', '-reoccurring', choices=['daily', 'weekly', 'bi-weekly', 'monthly', 'yearly'], default='0', dest='reoccurring')


def setup_expense_cmd(subparsers):
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


def setup_income_cmds(subparsers):
    parser_income = subparsers.add_parser('income')

    parser_income.add_argument(type=str,  nargs='?', dest='income')

    parser_income.add_argument(
        '-a', '-amount', type=float, nargs='?', dest='amount', required=True)

    parser_income.add_argument(
        '-d', '-date', type=str, nargs='?', dest='date', required=True)

    parser_income.add_argument(
        '-r', '-reoccurring', choices=['daily', 'weekly', 'bi-weekly', 'monthly', 'yearly'], default='none', dest='reoccurring')
