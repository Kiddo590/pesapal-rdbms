from core.parser.ast import CreateTable, Insert, Select

def parse(tokens):
    command = tokens[0].upper()

    if command == "SELECT":
        return Select(tokens[-1])

    raise NotImplementedError("Only SELECT supported for now")
