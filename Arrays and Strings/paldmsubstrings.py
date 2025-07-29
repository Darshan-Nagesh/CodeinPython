#Program to fins all palindromice substrings
def palsub(s):
    n = len(s)
    res = set()
    for i in range(n):
        left = right = i
        while left >= 0 and right <n and s[left] == s[right]:
            res.add(s[left:right+1])
            left -= 1
            right += 1
        left = i
        right = i+1
        while left >= 0 and right <n and s[left] == s[right]:
            res.add(s[left:right+1])
            left -= 1
            right += 1
    return res

inpstr = 'ababba'
res = palsub(inpstr)
print(f"Palindromic substrings: {res}")