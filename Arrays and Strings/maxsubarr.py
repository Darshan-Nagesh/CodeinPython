#Program to find maximum subarrray - Kandane's algorithm
def maxsub(a):
    cursum = a[0]
    maxsum = a[0]
    for i in a[1:]:
        cursum = max(i,cursum+i)
        maxsum = max(maxsum,cursum)
    return maxsum

a = [1,9,3,-4,-2,5,6,2]
res = maxsub(a)
print(f"Maximum sum of subarray = {res}")