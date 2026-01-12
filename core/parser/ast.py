# Base class
class ASTNode:
    pass


# ---- COLUMN DEFINITION ----
class ColumnDef(ASTNode):
    def __init__(self, name, col_type, primary=False, unique=False):
        self.name = name.lower()
        self.col_type = col_type.upper()
        self.primary = primary
        self.unique = unique

    def __repr__(self):
        flags = []
        if self.primary:
            flags.append("PRIMARY KEY")
        if self.unique:
            flags.append("UNIQUE")

        return f"{self.name} {self.col_type} {' '.join(flags)}".strip()


# ---- CREATE TABLE ----
class CreateTable(ASTNode):
    def __init__(self, table_name, columns):
        self.table_name = table_name.lower()
        self.columns = columns

    def __repr__(self):
        cols = ", ".join(str(c) for c in self.columns)
        return f"CREATE TABLE {self.table_name} ({cols})"


# ---- INSERT ----
class Insert(ASTNode):
    def __init__(self, table_name, values):
        self.table_name = table_name.lower()
        self.values = values

    def __repr__(self):
        return f"INSERT INTO {self.table_name} VALUES {self.values}"


# ---- SELECT ----
class Select(ASTNode):
    def __init__(self, columns, table_name, where=None):
        self.columns = columns
        self.table_name = table_name.lower()
        self.where = where

    def __repr__(self):
        return f"SELECT {self.columns} FROM {self.table_name}"
