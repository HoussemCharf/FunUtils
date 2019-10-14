# Input:
# 2
# 5
# 1 2 3 4 5
# 6
# 2 4 6 7 5 1
#
# Output:
# 3
# 7

def findMid(head):
    if head == None:
        return -1

    fast, slow = head, head

    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next

    if fast.next != None:
        return slow.next
    return slow
