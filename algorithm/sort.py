# quick sort
def quicksort(arr):
    if(len(arr) < 2):
        return arr
    else:
        pivot = arr[0]
        pre = [i for i in arr[1:] if i<=pivot]
        beh = [i for i in arr[1:] if i>pivot]
        return quicksort(pre) + [pivot] + quicksort(beh)

# merge sort
def merge(a, b):
    c = list()
    i = j = 0
    while(i < len(a) and j < len(b)):
        if(a[i] < b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if(i < len(a)):
        for x in a[i:]:
            c.append(x)
    else:
        for x in b[j:]:
            c.append(x)
    return c

def mergesort(arr):
    if(len(arr) < 2):
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)
    
if(__name__ == "__main__"):
    # print (quicksort([1,7,5,6,9,0,3,5,4,2]))
    # print(merge([1,2,3], [4,5,6]))
    print(mergesort([5,6,3,4,1,2]))

