def validate(eqn: str):
    brackets_map = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    stack = []

    for c in eqn:
        if c in brackets_map:
            stack.append(c)

        if c in brackets_map.values():
            top = stack.pop()
            if c != brackets_map[top]:
                return False
    return True


print(validate('{(a+b)}(a-b)'))
print(validate('{(a+b})(a-b)'))
