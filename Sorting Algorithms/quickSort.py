from random import randrange

def quickSort(arr):

    if len(arr) <= 1:
        return arr

    n = len(arr)
    pivot = randrange(n)
    arr[0], arr[pivot] = arr[pivot], arr[0]

    i = 1

    for j in range(1, n):
        if arr[j] < arr[0]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[0], arr[i-1] = arr[i-1], arr[0]

    arr[:i-1] = quickSort(arr[:i-1])
    arr[i:] = quickSort(arr[i:])

    return arr


if __name__=="__main__":

    print("Input the array to be sorted:")
    arr = list(map(int, input().split()))
    print(arr)
    print(quickSort(arr))
