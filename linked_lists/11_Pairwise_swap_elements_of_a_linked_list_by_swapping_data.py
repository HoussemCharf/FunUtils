# Input:
# 1
# 8
# 1 2 2 4 5 6 7 8
#
# Output:
# 2 1 4 2 6 5 8 7

def pairWiseSwap(head):

    if head == None or head.next == None:
        return head

    prev = None
    cur = head

    count = 2
    while count > 0 and cur != None:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
        count -= 1
    head.next = pairWiseSwap(cur)

    return prev
