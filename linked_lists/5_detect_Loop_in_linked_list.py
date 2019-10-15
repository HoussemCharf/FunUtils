# Input:
# 2
# 3
# 1 3 4
# 2
# 4
# 1 8 3 4
# 0
#
# Output:
# True
# False

def detectLoop(head):

    f_pointer = head
    s_pointer = head

    while f_pointer.next != None and f_pointer.next.next != None:
        f_pointer = f_pointer.next.next
        s_pointer = s_pointer.next
        if f_pointer == s_pointer:
            return 1

    return 0
