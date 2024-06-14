'''
Fibonacci Search is a comparison-based technique 
that uses Fibonacci numbers to search an element in a sorted array.
'''
def fibonacci_search(arr, val):
    # Initialize fibonacci numbers  
    fib_N_2 = 0 # (m-2)'th Fibonacci No
    fib_N_1 = 1 # (m-1)'th Fibonacci No.
    fibNext = fib_N_1 + fib_N_2 # m'th Fibonacci 

    length = len(arr)
    if length == 0:
        return 0
    
    # fibNext is going to store the smallest  
    # Fibonacci Number greater than or equal to array's length  
    while fibNext < len(arr):
        fib_N_2 = fib_N_1
        fib_N_1 = fibNext
        fibNext = fib_N_1 + fib_N_2
    
    # Marks the eliminated range from front
    index = -1

    # while there are elements to be inspected. 
    # Note that we compare arr[fib_N_2] with x. 
    # When fibNext becomes 1, fib_N_2 becomes 0 
    while fibNext > 1:

        # Check if fib_N_2 is a valid location 
        i = min(index + fib_N_2, (length - 1))

        if arr[i] < val:
            fibNext = fib_N_1
            fib_N_1 = fib_N_2
            fib_N_2 = fibNext - fib_N_1
            index = i
        elif arr[i] > val:
            fibNext = fib_N_2
            fib_N_1 = fib_N_1 - fib_N_2
            fib_N_2 = fibNext - fib_N_1
        else:
            return i

    # comparing the last element with x */        
    if (fib_N_1 and index < length - 1) and (arr[index + 1] == val):
        return index + 1
    
    # element not found. return -1
    return -1