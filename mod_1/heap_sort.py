

#   My own implementation of tree
#   it consists of set_left,set_right and add_next functions (self_explanatory)


class tree():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    
    def set_left(self,value):
        new_leaf = tree(value)
        self.left = new_leaf
        return new_leaf

    def set_right(self,value):
        new_leaf = tree(value)
        self.right = new_leaf
        return new_leaf
    
    def add_next(self,value):
        queue = [self]  
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = tree(value)
                return
            else:
                queue.append(node.left)
            if node.right is None:  
                node.right = tree(value)
                return
            else:
                queue.append(node.right)
    
    def print_tree(self,head):
        limit = 2
        i = 1
        queue = []
        queue.append(head)
        print(head.val)
        while queue:
            target = queue.pop(0)
            # print("current target: " , target.val)
            if(target.left != None):
                queue.append(target.left)
                print(target.left.val,end = " ")
                if(target.right != None):
                    queue.append(target.right)
                    print(target.right.val, end = " ")
                    if(i+2 < limit):
                        i += 2
                    else:
                        print()
                        limit *= 2
                        i = 1


#   implementation of heapsort 

#   three convinience functions
def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return int((i-1)/2)



#   in heapsort, first of all, we have to swap elements in places so array can be represented
#   as compleate tree, where both children of every node are smaller 

#   heapify function that compares nodes with its children and swaps with higher child
#   after that it resursivly calls itself on swapped child to 'fix' inconsistencies if they arised
def heapify(Tab,n,i):
    r = right(i)
    l = left(i)
    max_ind = i
    if l < n and Tab[l] > Tab[max_ind]:
        max_ind = l
    
    if r < n and Tab[r] > Tab[max_ind]:
        max_ind = r

    if(max_ind != i):
        Tab[i],Tab[max_ind] = Tab[max_ind],Tab[i]
        heapify(Tab,n,max_ind)


#   build_heap function call heapify for every node, starting from end of array
#   after that, array can be represented as whole tree where, for every node, it's children are smaller

def build_heap(Tab):
    n = len(Tab)
    for i in range(parent(n-1),-1,-1):
        heapify(Tab,n,i)

#   in main function, first we call build_heap so we are ceratin that highest value
#   is on first level, then we swap highest value with last value
#   then we 'fix' rest of heap, excluding values that are arleady sorted
#   repeat until whole array is sorted

def heapsort(Tab):
    n = len(Tab)
    build_heap(Tab)
    for i in range(n-1,0,-1):
        Tab[0],Tab[i] = Tab[i],Tab[0]
        heapify(Tab,i,0)
    

tab = [15, 75, 41, 2, 25, 16, 77, 72, 37, 14, 62, 67, 93, 25, 87]
print()
print("Array before sorting")
print(tab)

build_heap(tab)

print()
print("Array after 'heapfiying'")
print(tab)

t = tree(tab[0])

for i in range(1,len(tab)):
    t.add_next(tab[i])
 
print()
print("array represented as complete tree")
t.print_tree(t)

heapsort(tab)

print()
print("array after heap sorting")
print(tab)