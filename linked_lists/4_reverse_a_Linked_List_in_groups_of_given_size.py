# Input:
# 1
# 8
# 1 2 2 4 5 6 7 8
# 4
#
# Output:
# 4 2 2 1 8 7 6 5

def reverse(head, k):
    cur     = head
    prev    = None
    i       = k

    while i > 0 and cur is not None:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
        i -= 1

    if temp is not None:
        head.next = reverse(temp,  k)

    return prev
