def add_two_nums(n1: str, n2: str):
    res = []
    carry = 0
    i1, i2 = len(n1) - 1, len(n2) - 1
    while i1 >= 0 or i2 >= 0:
        m1 = ord(n1[i1]) - ord('0') if i1 >= 0 else 0
        m2 = ord(n2[i2]) - ord('0') if i2 >= 0 else 0

        val = (m1 + m2 + carry) % 10
        carry = (m1 + m2 + carry) // 10
        res.append(val)
        i1 -= 1
        i2 -= 1

    if carry > 0:
        res.append(carry)

    return ''.join([str(n) for n in list(reversed(res))])


addition = add_two_nums('1', '9')
print(addition)
