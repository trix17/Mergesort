def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) / 2

        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            arr[k] = L[i]
            i = i + 1

        else:
            arr[k] = R[j]
            j = j + 1
        k = k + 1

        while i < len(L):
            arr[k]= L[i]
            i = i + 1
            k = k + 1

        while j < len(R):
            arr[k] = R[i]
            j = j + 1
            k = k + 1
def printlist(arr):
    for i in range (len(arr)):
        print(arr[i], end="")
        print()
//Test the code

arr = [17,14,2,19,12,3]
print("The original array is",end="\n")
printlist()
mergeSort(arr)
print(" The sorted array is:", end= "\n")
printlist(arr)
