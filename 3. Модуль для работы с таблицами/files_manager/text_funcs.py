from tabulate import tabulate


def save_table(table, filename):
    with open(filename, 'w') as f:
        table = table.lst()
        f.write(tabulate(table[1:], headers=table[0], tablefmt="grid", stralign='center'))
