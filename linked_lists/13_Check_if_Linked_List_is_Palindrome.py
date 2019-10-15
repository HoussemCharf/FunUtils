# Input
# 2
# 3
# 1 2 1
# 4
# 1 2 3 4
#
# Output:
# 1
# 0

def isPalindrome(head):

    cur = head
    arr = []
    while cur is not None:
        arr.append(cur.data)
        cur = cur.next

    cur = head
    while cur is not None:
        if cur.data != arr.pop():
            return 0
        cur = cur.next
    return 1
