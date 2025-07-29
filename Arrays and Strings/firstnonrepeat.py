#Program to find the first non-repeating character
arr = [1,2,3,4,1,2,5,3]
schar = "america"
nonrpt = {}
for i in arr:
    nonrpt[i] = nonrpt.get(i,0) + 1
for i in arr:
    if nonrpt.get(i) == 1:
        print(f"First non-repeat element is {i}")
        break
nonrpt.clear()
for i in schar:
    nonrpt[i] = nonrpt.get(i,0) + 1
for i in schar:
    if nonrpt.get(i) == 1:
        print(f"First non-repeat character is {i}")
        break



