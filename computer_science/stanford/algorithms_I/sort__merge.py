sorted1 = [1,2,3]
sorted2 = [10,20,30]

def sort_merge(a1, a2):
    result = []
    n = len(sorted1) + len(sorted2)
    i, j = 0, 0
    for k in range(n):
        if a1[i] < a2[j]:
            result.append(a1[i])
            i = i + 1
        else:
            result.append(a2[j])
            j = j + 1
    return result
    
print(sort_merge(sorted1,sorted2))