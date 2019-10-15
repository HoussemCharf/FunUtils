# Input:
# 1
# 6
# 1 2 3 4 5 6
#
# Output:
# 6 5 4 3 2 1

def reverseList(self):
    if self.head is None:
        return None

    prev    = None
    cur     = self.head

    while cur != None:
        temp        = cur.next
        cur.next    = prev
        prev        = cur
        cur         = temp

    self.head = prev
