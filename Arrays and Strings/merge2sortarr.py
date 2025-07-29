#Program to merge two sorted arrays

def mergesort(a,b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c

a = [1,2,4,6,7,8]
b = [1,2,3,5,9,10]
i = j = 0
res = mergesort(a,b)
print(f'Merge sorted arrays: {res}')
