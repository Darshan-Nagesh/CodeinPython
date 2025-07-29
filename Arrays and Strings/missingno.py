#program to find missing no in an array
arr = [1,2,4,5,6]
n = len(arr)+1
totarrsum = sum(arr)
totexsum = n * (n+1) // 2
mis = totexsum - totarrsum
print(f'Missing no. = {mis}')
