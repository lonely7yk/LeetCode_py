# recursive
def quickPow1(a, b):
    """
    @param a: base
    @param b: exponential
    @return a^b
    """
    if a == 0: return 0
    if a == 1 or b == 0: return 1
    
    tmp = quickPow1(a, b // 2)
    return tmp * tmp if b % 2 == 0 else tmp * tmp * a

# iterative
def quickPow2(a, b):
    """
    @param a: base
    @param b: exponential
    @return a^b
    """
    if a == 0: return 0

    res = 1
    base = a
    while b:
        if b & 1: res *= base
        base = base * base
        b = b >> 1

    return res

# add mode
def quickPowMode1(a, b, mode):
    if a == 0: return 0
    if a == 1 or b == 0: return 1

    tmp = quickPowMode1(a, b // 2, mode)
    res = tmp * tmp % mode
    return res if b % 2 == 0 else res * a % mode

def quickPowMode2(a, b, mode):
    if a == 0: return 0

    res = 1
    base = a
    # 可以对 res 和 base 都用取模是因为 (a * b) % c = ((a % c) * (b % c)) % c
    while b:
        if b & 1: res = res * base % mode
        base = base * base % mode
        b = b >> 1

    return res


print(quickPow1(71, 80))
print(quickPow2(71, 80))
print(quickPowMode1(71, 80, 10 ** 9))
print(quickPowMode2(71, 80, 10 ** 9))

