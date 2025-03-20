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


def merge(l1,l2):
    if(l1 == None):
        return l2
    if(l2 == None):
        return l1

    if l1.val > l2.val:
        l2.next = merge(l1,l2.next)
        return l2
    else:
        l1.next = merge(l1.next,l2)
        return l1
    
def serie(head):
    if head is None:
        return None
    curr = head
    while curr.next is not None:
        if curr.val <= curr.next.val:
            curr = curr.next
        else:
            second = curr.next
            curr_2 = second
            while curr_2.next is not None:
                if curr_2.val <= curr_2.next.val:
                    curr_2= curr_2.next
                else:
                    curr_2 = curr_2.next
                    return head.second,curr_2
                    



head1 = node(5)
head1.appendn(6)
head1.appendn(7)
head1.appendn(10)


head2 = node(0)
head2.appendn(2)
head2.appendn(8)
head2.appendn(9)
head2.appendn(11)

head = node(None)
head = merge(head1,head2)
head.printn()