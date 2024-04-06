def calculator(expressions):
    allowed = '+-*/'
    if not any(sign in expressions for sign in allowed):
        raise ValueError(f'Выражение должно содерджать хотя бы один знак {allowed}')

    for sign in allowed:
        if sign in expressions:
            try:
                left, right = expressions.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                }[sign](left, right)
            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать 2 целые числа и 1 знак')


if __name__ == '__main__':
    print(calculator('2+8'))
