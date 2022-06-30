from files_manager.print_t import print_table
from files_manager.csv_funcs import *
from files_manager.pickle_funcs import save_table as s_pickle
from files_manager.pickle_funcs import load_table as l_pickle
from files_manager.text_funcs import save_table as s_text

if __name__ == '__main__':
    # table loadings and savings
    table1 = load_table('1.csv', set_correct_type=True)
    # print(print_table(table1))
    # save_table(table1, 'table1.csv')
    # s_pickle(table1, 'pickle1.meow')
    # table2 = l_pickle('pickle1.meow')
    # s_text(table2, 'table2.txt')

    # multiple loading
    # multi_table = load_table('1.csv', '2.csv', set_correct_type=True)
    # print(print_table(multi_table))
    # save_table(multi_table, max_rows=3)
    # multi_table_2 = load_table('0_default.csv', '4_default.csv')
    # print(print_table(multi_table_2))

    # concat and split
    # print(print_table(concat(table1, multi_table_2)))
    # spl1, spl2 = split(multi_table, row_number=2)
    # print(print_table(spl1))
    # print(print_table(spl2))

    # defining column type
    # print(multi_table.get_column_types())

    # №7: eq (==), gr (>), ls (<), ge (>=), le (<=), ne (!=)
    # bool_list = le(multi_table, 3, 4)
    # print(print_table(filter_rows(multi_table, bool_list, 3, 4)))

    # base functions
    # rows_copy = multi_table.get_rows_by_number(start=1, copy_table=True)
    # print(print_table(rows_copy))

    # rows_copy = multi_table.get_rows_by_index(1, 5, 10)
    # print(print_table(rows_copy))

    # print(multi_table.get_column_types())

    # multi_table.set_columns_types({0: int, 1: str, 2: str, 3: int, 4: float}, by_number=True)
    # print(multi_table.get_column_types())

    # print(multi_table.get_values(1))

    # print(multi_table.get_value(3))

    # multi_table.set_values([312, 81, 3, 42, -5])
    # print(print_table(multi_table))

    # multi_table.set_value(111, column=4)
    # print(print_table(multi_table))
