#Program to find the indices of two elements in an array whose sum is equal to required value
def twosum(arr,target):
    visited = {}
    for ind, val in enumerate(arr):
        complement = target - val
        if complement in visited:
            return [visited[complement],ind]
        visited[val] = ind

arr = [1,2,4,6,8,3]
target = 8
res = twosum(arr, target)
print(f"Indices that sums upto {target} : {res}")