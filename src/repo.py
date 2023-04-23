import sqlite3
import os

db_location = "money_py.db"

if os.environ.get('MY_APP_ENV') == 'test':
    db_location = "test/money_py_test.db"

def setup_db():
    con = sqlite3.connect(db_location)
    cur = con.cursor()
    cur.executescript("""
    create table if not exists expenses(
        expense_id INTEGER PRIMARY KEY,
        product_service varchar(30) not null,
        seller varchar(30),
        price float not null,
        purchase_date datetime not null,
        category_id int,
        foreign key (category_id) references budget(budget_id)
    );
    create table if not exists budgets(
        budget_id INTEGER PRIMARY KEY,
        name varchar(30) not null,
        budegt_date date not null,
        budget_amount float not null,
        constraint uc_category unique (name, budegt_date)
    );
    """)
    cur.close()


def add_budget_category(budget_name: str, budget_period: str, budget_amount: float):
    con: sqlite3.Connection = sqlite3.connect(db_location)
    cur: sqlite3.Cursor = con.cursor()

    cur.execute("""
    insert into budgets(name, budegt_date, budget_amount)
    values(?, ?, ?)
    """, (budget_name, budget_period, budget_amount))

    con.commit()
    con.close()


def add_expense(product_service: str, seller: str, price: float, purchase_date: str, budget_name: str):
    con: sqlite3.Connection = sqlite3.connect(db_location)
    cur: sqlite3.Cursor = con.cursor()

    cur.execute("""
    insert into expenses(product_service, seller, price, purchase_date, category_id)
    select ?, ?, ?, (?) as cur_year, b.budget_id
    from budgets b
    where b.name = ?
    and cur_year = strftime('%Y', b.budegt_date)
    """, (product_service, seller, price, purchase_date, budget_name))

    con.commit()
    con.close()


def select_expenses(expense_name: str, seller: str, category: str) -> list[tuple]:
    con: sqlite3.Connection = sqlite3.connect(db_location)
    cur: sqlite3.Cursor = con.cursor()

    expenses = cur.execute("""
    select e.product_service, e.seller, e.price, e.purchase_date, b.name
    from expenses e
    join budgets b on b.budget_id = e.category_id
    where e.product_service like ?
    and e.seller like ?
    and b.name like ?
    """, (f'%{expense_name}%', f'%{seller}%', f'%{category}%')).fetchall()

    con.close()
    return expenses

