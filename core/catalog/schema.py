class Column:
    def __init__(self, name, col_type, primary=False, unique=False):
        self.name = name
        self.col_type = col_type
        self.primary = primary
        self.unique = unique


class TableSchema:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.primary_key = None

        for col in columns:
            if col.primary:
                self.primary_key = col.name
