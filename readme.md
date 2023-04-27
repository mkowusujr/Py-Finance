# Py Finance
![logo](logo.png)

A simple budget tracking terminal app written in python

This was built with:
- [sqlite3](https://docs.python.org/3/library/sqlite3.html)
- the [argparse](https://docs.python.org/3/library/argparse.html#module-argparse) python library for making CLIs
- my brain B)

# Creating Entries
> When typing in input that is multiply string, wrap in quotes to prevent issues

## Adding Budget

```shell
python main.py budget Groceries -amount 100.00 -date 2023/04/23
```

The shortened command
```shell
python main.py Groceries -a 100.00 -d 2023/04/23
```

## Adding Entries
Entries represent an expense
```shell
python main.py expense Groceries -seller Walmart -amount 36.99 -date 2023/04/23 -category Groceries
```

shortened command
```shell
python main.py expense Groceries -s Walmart -a 36.99 -d 2023/04/23 -c Groceries
```

# Viewing Entries
## list all Entries
```shell
python main.py list expenses
```

You can filter the results by adding option args
```shell
python main.py list expenses -seller Steam -expense Jedi -category Enterntainment 
```

```shell
python main.py list expenses -s Steam -e Jedi -c Enterntainment 
```

```shell
python main.py list budgets
```

```shell
python main.py list budgets -b Groceries
```