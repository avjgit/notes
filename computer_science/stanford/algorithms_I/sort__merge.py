def sort_merge(a1, a2):
    
    result = []
    
    n = len(a1) + len(a2)
    
    i, j = 0, 0
    
    for k in range(n):
        if (i < len(a1)) and (a1[i] < a2[j]):
            result.append(a1[i])
            i = i + 1
        else:
            result.append(a2[j])
            j = j + 1
    return result

sorted1 = [1,2,3]
sorted2 = [10,20,30]
print(sort_merge(sorted1,sorted2))

sorted1 = [1,3,5]
sorted2 = [2,4,6]
print(sort_merge(sorted1,sorted2))

sorted1 = [1,4,8]
sorted2 = [2,3,9]
print(sort_merge(sorted1,sorted2))