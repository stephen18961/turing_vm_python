def parse(expression):
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    return read_tokens(tokens)

def parse_words(expression):
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    return tokens

def read_tokens(tokens):
    if len(tokens) == 0:
        raise SyntaxError("Unexpected EOF")

    token = tokens.pop(0)

    if token == '(':
        subexpression = []
        while tokens[0] != ')':
            subexpression.append(read_tokens(tokens))
        tokens.pop(0)  # Discard ')'
        return subexpression
    elif token == ')':
        raise SyntaxError("Unexpected )")
    else:
        return atom(token)

def atom(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token

def evaluate(expression):
    if isinstance(expression, list):
        # If it's a list, it's a subexpression
        operator = expression[0]
        operands = expression[1:]
        if operator == '+':
            return sum(evaluate(operand) for operand in operands)
        elif operator == '*':
            result = 1
            for operand in operands:
                result *= evaluate(operand)
            return result
        else:
            raise ValueError(f"Unknown operator: {operator}")
    else:
        # If it's not a list, it's an atomic value (number or symbol)
        return expression

if __name__ == "__main__":
    # Example usage
    expression = "(* 3 (+ 1 2))"
    parsed_expression = parse(expression)
    result = evaluate(parsed_expression)
    print(result)