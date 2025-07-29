#program to find whether string is palindrome
strw = "olleh hello"
'''rstrw = strw[::-1]
if strw == rstrw:
    print(f'{strw} is palindrome')
else:
    print(f'{strw} is not palindrome since its reverse is {rstrw}')'''
flag = 1
for i in range(len(strw)//2):
    if strw[i] != strw[len(strw)-1-i]:
        flag = 0
if flag:
    print(f'{strw} is palindrome')
else:
    print(f'{strw} is not palindrome')

