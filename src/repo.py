import sqlite3
import os

db_location = "finance.db"

if os.environ.get('MY_APP_ENV') == 'test':
    db_location = "test/finance_test.db"


def setup_db():
    con = sqlite3.connect(db_location)
    cur = con.cursor()
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS expenses(
        expense_id INTEGER PRIMARY KEY,
        expense_name TEXT NOT NULL,
        seller TEXT,
        price REAL NOT NULL,
        purchase_date TEXT NOT NULL,
        category_id INTEGER,
        is_reoccurring TEXT,
        foreign key (category_id) references budget(budget_id)
    );
    CREATE TABLE IF NOT EXISTS budgets(
        budget_id INTEGER PRIMARY KEY,
        budget_name TEXT NOT NULL,
        budget_date TEXT NOT NULL,
        budget_amount REAL NOT NULL,
        is_reoccurring TEXT,
        constraint uc_category unique (budget_name, budget_date)
    );
    CREATE TABLE IF NOT EXISTS incomes(
        income_id INTEGER PRIMARY KEY,
        income_name TEXT,
        income_amount REAL,
        income_date TEXT,
        is_reoccurring TEXT
    );
    """)
    cur.close()


def add_budget(budget_name: str, budget_period: str, budget_amount: float, reoccurring: str):
    con: sqlite3.Connection = sqlite3.connect(db_location)
    cur: sqlite3.Cursor = con.cursor()

    cur.execute("""
    insert into budgets(budget_name, budget_date, budget_amount, is_reoccurring)
    values(?, ?, ?, ?)
    """, (budget_name, budget_period, budget_amount, reoccurring))

    con.commit()
    con.close()


def add_expense(expense_name: str, seller: str, price: float, purchase_date: str, budget_name: str, reoccurring: str):
    con: sqlite3.Connection = sqlite3.connect(db_location)
    cur: sqlite3.Cursor = con.cursor()

    cur.execute("""
    insert into expenses(expense_name, seller, price, purchase_date, is_reoccurring, category_id)
    select ?, ?, ?, ?, ?, b.budget_id
    from budgets b
    where b.budget_name = ?
    """, (expense_name, seller, price, purchase_date, reoccurring, budget_name))

    con.commit()

    spent = cur.execute("""
    select sum(e.price) as total
    from expenses e
    join budgets b on b.budget_id = e.category_id
    where b.budget_name = ?
    """, [budget_name]).fetchone()[0]
    
    budget = cur.execute("""
    select b.budget_amount
    from budgets b
    where b.budget_name = ?
    """, [budget_name]).fetchone()[0]

    con.close()

    return budget, spent, budget - spent


def add_income(income_name: str,  income_amount: float, income_date: str, reoccurring: str):
    con: sqlite3.Connection = sqlite3.connect(db_location)
    cur: sqlite3.Cursor = con.cursor()

    cur.execute("""
    insert into incomes(income_name, income_amount, income_date, is_reoccurring)
    values(?, ?, ?, ?)
    """, (income_name, income_amount, income_date, reoccurring))

    con.commit()
    con.close()


def select_expenses(expense_name: str, seller: str, category: str) -> list[tuple]:
    con: sqlite3.Connection = sqlite3.connect(db_location)
    cur: sqlite3.Cursor = con.cursor()

    expenses = cur.execute("""
    select e.expense_name, e.seller, e.price, e.purchase_date, b.budget_name, b.is_reoccurring
    from expenses e
    join budgets b on b.budget_id = e.category_id
    where e.expense_name like ?
    and e.seller like ?
    and b.budget_name like ?
    """, (f'%{expense_name}%', f'%{seller}%', f'%{category}%')).fetchall()

    con.close()
    return expenses


def select_budgets(budget_name: str) -> list[tuple]:
    con: sqlite3.Connection = sqlite3.connect(db_location)
    cur: sqlite3.Cursor = con.cursor()

    budgets = cur.execute("""
    select b.budget_name, b.budget_amount, b.budget_date, b.is_reoccurring
    from budgets b
    where b.budget_name like ?
    """, [f'%{budget_name}%']).fetchall()

    con.close()
    return budgets


def select_incomes(income_name: str) -> list[tuple]:
    con: sqlite3.Connection = sqlite3.connect(db_location)
    cur: sqlite3.Cursor = con.cursor()

    incomes = cur.execute("""
    select i.income_name, i.income_amount, i.income_date, i.is_reoccurring
    from incomes i
    where i.income_name like ?
    """, [f'%{income_name}%']).fetchall()

    con.close()
    return incomes


def select_reoccurring(search_term: str, show_e: bool, show_b: bool, show_i: bool) -> list[tuple]:
    con: sqlite3.Connection = sqlite3.connect(db_location)
    cur: sqlite3.Cursor = con.cursor()

    expenses = cur.execute("""
    select e.expense_name, e.seller, e.price, e.purchase_date, b.budget_name, b.is_reoccurring
    from expenses e
    join budgets b on b.budget_id = e.category_id
    where e.is_reoccurring != 'none'
    and e.expense_name like ?
    """, [f'%{search_term}%']).fetchall()

    budgets = cur.execute("""
    select b.budget_name, b.budget_amount, b.budget_date, b.is_reoccurring
    from budgets b
    where b.is_reoccurring != 'none'
    and b.budget_name like ?
    """, [f'%{search_term}%']).fetchall()

    incomes = cur.execute("""
    select i.income_name, i.income_amount, i.income_date, i.is_reoccurring
    from incomes i
    where i.is_reoccurring != 'none'
    and i.income_name like ?
    """, [f'%{search_term}%']).fetchall()

    con.close()
    return expenses if show_e else [], budgets if show_b else [], incomes if show_i else []
