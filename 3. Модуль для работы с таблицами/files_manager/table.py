from copy import deepcopy


class TableMetadata:
    def __init__(self, fieldnames):
        self.fieldnames = fieldnames
        self.column_types = [[x, str] for x in fieldnames]

    def column_type(self, index):
        return self.column_types[index][1]

    def __deepcopy__(self, memodict={}):
        md = TableMetadata(self.fieldnames)
        md.column_types = deepcopy(self.column_types)
        return md


class Table:
    def __init__(self, fieldnames, rows=None, metadata=None):
        if rows is None:
            rows = []
        self.metadata = metadata if metadata else TableMetadata(fieldnames)
        self.rows = []
        for row in rows:
            self.append_row(row)

    def append_row(self, row):
        if isinstance(row, Row):            
            self.rows.append(row)
        else:
            self.rows.append(Row(row, len(self.rows), self.metadata))

    def __getitem__(self, item):
        return self.rows[item]

    def lst(self):
        list_ = [self.metadata.fieldnames]
        for row in self.rows:
            list_.append([str(x) for x in row.data.values()])
        return list_

    def __len__(self):
        return len(self.rows)

    def get_rows_by_number(self, start, stop=None, copy_table=False):
        stop = stop if stop else len(self.rows)
        rows = deepcopy(self.rows[start:stop]) if copy_table else self.rows[start:stop]
        metadata = deepcopy(self.metadata) if copy_table else self.metadata
        return Table(self.metadata.fieldnames, rows, metadata=metadata)

    def get_rows_by_index(self, *vals, copy_table=False):
        try:
            rows = []
            for ix in vals:
                row = deepcopy(self.rows[ix]) if copy_table else self.rows[ix]
                rows.append(row)
            return Table(self.metadata.fieldnames, rows, self.metadata)
        except IndexError:
            raise Exception("Один из индексов отсылает на несуществующую строку")

    def get_column_types(self, by_number=True):                                  
        resp = dict()
        if by_number:
            for ix, (name, type) in enumerate(self.metadata.column_types):
                resp[ix] = type
        else:
            for name, type in self.metadata.column_types:
                resp[name] = type
        return resp

    def set_column_type(self, key, type):
        for row in self.rows:
            try:
                row.data[key] = type(row.data[key])
            except ValueError:
                raise Exception(f'Невозможно привести к типу {type} колонку {key}')
        for item in self.metadata.column_types:
            if item[0] == key:
                item[1] = type

    def set_columns_types(self, types_dict, by_number=True):
        if len(types_dict) != len(self.metadata.column_types):
            raise Exception('Количество столбцов не совпадает')
        for k, v in types_dict.items():
            key = self.metadata.column_types[k][0] if by_number else k
            self.set_column_type(key, v)

    def get_value(self, column=0):
        try:
            return self.get_values(column)[0]
        except IndexError:
            raise Exception("Ошибка: Столбец с таким индексом не существует")

    def get_values(self, column=0):
        try:
            if isinstance(column, int):
                column = self.metadata.fieldnames[column]
            return list([x.data[column] for x in self.rows])
        except IndexError:
            raise Exception("Ошибка: Столбец с таким индексом не существует")

    def set_values(self, values, column=0):
        try:
            if isinstance(column, int):
                column = self.metadata.fieldnames[column]
            for val, row in zip(values, self.rows):
                row.data[column] = val
        except IndexError:
            raise Exception("Ошибка: Столбец с таким индексом не существует")
        except BaseException:
            raise Exception("Непредвиденная ошибка")

    def set_value(self, value, column=0):
        try:
            if isinstance(column, int):
                column = self.metadata.fieldnames[column]
            self.rows[0].data[column] = value
        except IndexError:
            raise Exception("Ошибка: Столбец с таким индексом не существует")
        except BaseException:
            raise Exception("Непредвиденная ошибка")


class Row:
    def __init__(self, data, ix, metadata):
        self.data = {k: metadata.column_type(ix)(v) for ix, (k, v) in enumerate(data.items())}
        self.ix = ix
        self.metadata = metadata

    def __getitem__(self, item):
        return self.data[item]

    def __deepcopy__(self, memodict={}):
        return Row(deepcopy(self.data), self.ix, deepcopy(self.metadata))
