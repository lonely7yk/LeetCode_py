def findNext(pattern):
    n = len(pattern)
    next = [0 for i in range(n)]

    j = 0
    i = 1

    while i < n:
        if pattern[i] == pattern[j]:
            next[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                next[i] = 0
                i += 1
            else:
                j = next[j - 1]

    return next

def kmp(s, p, next):
    i, j = 0, 0
    m = len(s)
    n = len(p)

    while i < m:
        if s[i] == p[j]:
            i += 1
            j += 1
            # 模式串全部匹配
            if j == n:
                return i - j
        else:
            if j == 0:
                i += 1
            else:
                j = next[j - 1]

    return -1


s = "abxabxaaanbcabc"
pattern = "abc"
next = findNext(pattern)
idx = kmp(s, pattern, next)
print(idx)
