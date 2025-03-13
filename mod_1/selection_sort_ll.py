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




head = node(5)
head.appendn(8)
head.appendn(2)
head.appendn(6)
head.appendn(9)
head.appendn(0)

head.printn()

def selection_sort(first):
    a = first
    while(a != None):
        min_value = a.val
        min_index = a
        b = a
        while(b != None):
            if(b.val < min_value):
                min_value = b.val
                min_index = b
            b = b.next

        min_index.val,a.val = a.val,min_index.val

        a = a.next
        
    first.printn()

selection_sort(head)