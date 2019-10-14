# Input:
# 2
# 9 2
# 1 2 3 4 5 6 7 8 9
# 4 5
# 10 -5 -100 5
#
#
# Output:
# 8
# -1

def getNthFromLast(head, n):

    cur = head
    while n > 1 and cur is not None:
        cur = cur.next
        n -= 1

    if cur == None:
        return -1

    new_cur = head
    while cur.next != None:
        new_cur = new_cur.next
        cur = cur.next

    return new_cur.data
