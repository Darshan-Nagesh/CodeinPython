#program to remove duplicates in sorted array
arr = [1,1,2,3,3,4,4,4,5]
print(f'Original array: {arr}')
res = [arr[0]]
for i in range(1,len(arr)):
    if arr[i] != arr[i-1]:
        res.append(arr[i])
print(f'Array after removing duplicates: {res}')