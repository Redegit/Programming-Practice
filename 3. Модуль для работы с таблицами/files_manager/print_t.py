from tabulate import tabulate


def print_table(table):
    try:
        table = table.lst()
    except AttributeError:
        raise Exception("Какая-то ошибка сделала невозможным вывод таблицы")
    return tabulate(table[1:], headers=table[0], tablefmt="grid", stralign='center')
