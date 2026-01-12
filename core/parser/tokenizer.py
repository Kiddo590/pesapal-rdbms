import re

# Regex explanation:
# 1. Strings: '...'
# 2. Identifiers / keywords
# 3. Numbers
# 4. Symbols: ( ) , *
TOKEN_REGEX = re.compile(
    r"""
    '([^']*)'            |  # strings
    (\b\d+\b)            |  # integers
    ([A-Za-z_][A-Za-z0-9_]*) |  # identifiers / keywords
    ([(),*])                 # symbols
    """,
    re.VERBOSE
)

def tokenize(sql: str):
    """
    Converts SQL string into a list of tokens.
    """
    tokens = []

    for match in TOKEN_REGEX.finditer(sql):
        token = next(group for group in match.groups() if group is not None)
        tokens.append(token.upper())

    return tokens
