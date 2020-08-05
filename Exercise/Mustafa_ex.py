a = [1,2,43,3,5,43,3,2,1,100,200,110,100,200,100,3,2,4,6,5,2,6,5,3,12,13,43,45,43]

counts = {}

for val in a:
    if not val in counts:
        counts[val] = 1
    else:
        counts[val] += 1

print(counts)