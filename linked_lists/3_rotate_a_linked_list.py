# Input:
# 1
# 8
# 1 2 3 4 5 6 7 8
# 4
#
# Output:
# 5 6 7 8 1 2 3 4

def rotateList(head, k):
    cur = head

    while k > 1:
        cur = cur.next
        k -= 1

    #when k is same as length of LL
    if cur.next == None:
        return head

    last_node   = cur
    new_head    = cur.next

    while cur.next != None:
        cur = cur.next

    cur.next        = head
    head            = new_head
    last_node.next  = None

    return head
