""" This algorithm allows you to enter values ​​that will be
inserted in an orderly way into the list """

n = int(input("How many numbers do you wanna insert in the list? "))
llist = []
for i in range(0, n):
    k = i
    value = int(input(f"\nChoose the {i+1}° value: "))
    if i == 0:
        llist.append(value)
        print("The value was added to the start of the list")
    elif value < llist[i-1]:
        while value < llist[k-1]:
            k = k-1
            if k == 0:
                llist.insert(k, value)
                print(f"The value was added to the position {k} of the list")
                break
            elif value >= llist[k-1]:
                llist.insert(k, value)
                print(f"The value was added to the position {k} of the list")
                break
    else:
        llist.append(value)
        print("The value was added to the end of the list")
print("\nSorted:", llist)
