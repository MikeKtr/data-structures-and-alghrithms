class node():
    def __init__(self,value):
        self.val = value
        self.next = None
    
    def appendn(first,value):
        while(first.next != None):
            first = first.next

        new_node = node(value)
        first.next = new_node

    def printn(first):
        print(first.val,end = "->")
        while(first.next != None):
            first = first.next
            print(first.val,end = "->")
        print("None")

def split(head):
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        if fast:
            slow = slow.next
            
    second = slow.next
    slow.next = None
    return second


def merge(l1,l2):
    
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    if l1.val < l2.val:
        l1.next = merge(l1.next,l2)
        return l1
    else:
        l2.next=merge(l1,l2.next)
        return l2

    
def merge_sort(head):
  

    if not head or not head.next:
        return head

    second = split(head)

    head = merge_sort(head)
    second = merge_sort(second)
    # print(head.val, second.val)
    return merge(head, second)


head = node(5)
head.appendn(8)
head.appendn(2)
head.appendn(6)
head.appendn(9)
head.appendn(0)
head.appendn(10)
head.appendn(3)

print("linked list before sorting:")
head.printn()
print("linked list after sorting:")
head = merge_sort(head)
head.printn()