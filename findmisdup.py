'''
Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs 
twice in the array, find both the duplicate number and the missing number.
'''

class Solution:
    def findTwoElement(self, arr):
        # code here
        n = len(arr)
        expsum = n * (n+1) // 2
        expsumseq = n * (n+1) * (2*n+1) // 6
        arrsum = sum(arr)
        arrsumseq = sum(x*x for x in arr)
        dif = arrsum - expsum
        difseq = arrsumseq - expsumseq
        sumxy = difseq // dif
        dup = (sumxy + dif) // 2
        mis = dup - dif
        res = [dup, mis]
        return res
