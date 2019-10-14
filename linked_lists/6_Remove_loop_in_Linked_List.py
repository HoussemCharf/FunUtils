# Input:
# 2
# 3
# 1 3 4
# 2
# 4
# 1 8 3 4
# 0
# Output:
# 1
# 1

def removeTheLoop(head):

    s_pointer = head
    f_pointer = head

    while f_pointer.next != None and f_pointer.next.next != None:
        s_pointer = s_pointer.next
        f_pointer = f_pointer.next.next

        if s_pointer == f_pointer:
            f_pointer.next = None
            return 1
    return 1
