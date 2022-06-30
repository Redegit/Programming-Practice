import csv
from files_manager.table import Table
from files_manager.print_t import print_table
from copy import deepcopy


def load_table(*file_path, delimiter=';', set_correct_type=False):
    for file in file_path:
        try:
            with open(file, 'r') as f:
                # класс DictReader отображает информацию о каждой строке в виде словаря {заголовок (из fieldnames): значение}
                csv_reader = csv.DictReader(f, delimiter=delimiter)
                if file == file_path[0]:
                    table = Table(csv_reader.fieldnames)
                    for row in csv_reader:
                        for k in row.keys():
                            if row[k] == '':
                                row[k] = None
                        table.append_row(row)
                elif csv_reader.fieldnames == table.metadata.fieldnames and file != file_path[0]:
                    for row in csv_reader:
                        table.append_row(row)
                else:
                    raise Exception('Структура столбцов файлов различна')
        except FileNotFoundError:
            raise Exception(f'Файл {file} не найден')
    if set_correct_type:
        type_check(table)
    return table


def save_table(table, filename='default.csv', delimiter=';', max_rows=0):
    try:
        if max_rows == 0:
            with open(filename, 'w', newline='') as f:
                csv_writer = csv.DictWriter(f, table.metadata.fieldnames, delimiter=delimiter)
                csv_writer.writeheader()
                for row in table:
                    csv_writer.writerow(row.data)
        else:
            for i in range(0, len(table), max_rows):
                save_table(table.get_rows_by_number(start=i, stop=i+max_rows), filename=f'{i//max_rows}_{filename}', delimiter=delimiter)
    except ValueError:
        raise Exception('Структура столбцов различна')


def concat(table1, table2):
    try:
        for row in table2:
            table1.append_row(row)
        return table1
    except BaseException:
        raise Exception("Что-то пошло не так")


def split(table, row_number):
    if row_number > len(table.metadata.fieldnames):
        raise Exception("Ошибка: Строки с таким индексом не существует")
    table1 = Table(fieldnames=table.metadata.fieldnames)
    table2 = Table(fieldnames=table.metadata.fieldnames)
    k = 0
    for row in table:
        table1.append_row(row)
        k += 1
        if k == row_number:
            break
    for row in table.get_rows_by_number(start=row_number):
        table2.append_row(row)
    return table1, table2


def type_check(table):
    dic = {x: str for x in table.metadata.fieldnames}
    for key in dic.keys():
        try:
            table.set_column_type(key, int)
        except Exception:
            try:
                table.set_column_type(key, float)
            except Exception:
                pass


def eq(table, col1, col2):
    try:
        c1 = table.get_values(col1)
        c2 = table.get_values(col2)
        bool_list = []
        for op1, op2 in zip(c1, c2):
            if op1 == op2:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list
    except (IndexError, TypeError):
        raise Exception("Ошибка: Один из индексов отсылается на несуществующий столбец")


def gr(table, col1, col2):
    try:
        c1 = table.get_values(col1)
        c2 = table.get_values(col2)
        bool_list = []
        for op1, op2 in zip(c1, c2):
            if op1 > op2:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list
    except (IndexError, TypeError):
        raise Exception("Ошибка: Один из индексов отсылается на несуществующий столбец")


def ls(table, col1, col2):
    try:
        c1 = table.get_values(col1)
        c2 = table.get_values(col2)
        bool_list = []
        for op1, op2 in zip(c1, c2):
            if op1 < op2:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list
    except (IndexError, TypeError):
        raise Exception("Ошибка: Один из индексов отсылается на несуществующий столбец")


def ge(table, col1, col2):
    try:
        c1 = table.get_values(col1)
        c2 = table.get_values(col2)
        bool_list = []
        for op1, op2 in zip(c1, c2):
            if op1 >= op2:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list
    except (IndexError, TypeError):
        raise Exception("Ошибка: Один из индексов отсылается на несуществующий столбец")


def le(table, col1, col2):
    try:
        c1 = table.get_values(col1)
        c2 = table.get_values(col2)
        bool_list = []
        for op1, op2 in zip(c1, c2):
            if op1 <= op2:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list
    except (IndexError, TypeError):
        raise Exception("Ошибка: Один из индексов отсылается на несуществующий столбец")


def ne(table, col1, col2):
    try:
        c1 = table.get_values(col1)
        c2 = table.get_values(col2)
        bool_list = []
        for op1, op2 in zip(c1, c2):
            if op1 != op2:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list
    except (IndexError, TypeError):
        raise Exception("Ошибка: Один из индексов отсылается на несуществующий столбец")


def filter_rows(table, bool_list, col1, col2, copy_table=False):
    try:
        ix = []
        for i in range(len(bool_list)):
            if bool_list[i]:
                ix.append(i)
        if copy_table:
            table = deepcopy(table)
        table = table.get_rows_by_index(*ix)
        return table
    except (IndexError, TypeError):
        raise Exception("Ошибка: Один из индексов отсылается на несуществующий столбец")