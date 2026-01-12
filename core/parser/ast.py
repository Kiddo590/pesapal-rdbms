class ASTNode:
    pass


class CreateTable(ASTNode):
    def __init__(self, table_name, columns):
        self.table_name = table_name
        self.columns = columns


class Insert(ASTNode):
    def __init__(self, table_name, values):
        self.table_name = table_name
        self.values = values


class Select(ASTNode):
    def __init__(self, table_name):
        self.table_name = table_name
