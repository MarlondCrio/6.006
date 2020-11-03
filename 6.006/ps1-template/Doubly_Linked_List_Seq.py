class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        if self.head == None:
            new_node = Doubly_Linked_List_Node(x)
            new_node.next = self.head
            self.tail = new_node
            self.head = new_node
    
        elif isinstance(self.head,Doubly_Linked_List_Node):

            new_node = Doubly_Linked_List_Node(x)
            new_node.next = self.head
            
            self.head.prev = new_node
            self.head = new_node

        ###########################
        pass

    def insert_last(self, x):
        n = self.head
        new_node = Doubly_Linked_List_Node(x)
        
        if self.head is None:
            #print('shhh', new_node.item)
            self.insert_first(x)
            
        
        else:

            new_node.prev = self.tail 
            self.tail.next = new_node
            self.tail = new_node
    def delete_first(self):
        #print('delete_fist')
        x = None
        #self.head.next.prev = x
        
        x = self.head.item 
        self.head = self.head.next
        self.head.prev = None
        ###########################
        return x

    def delete_last(self):
        #print('delete_last')

        x = None
        x = self.tail.item 

        self.tail.prev.next = None
        self.tail = self.tail.prev
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()

        if x1 == self.head:

            self.head = x2.next
            
            self.head.prev = None
        
        else:
            x1.prev.next = x2.next            
        L2.head = x1
        L2.tail = x2        
        L2.head.prev = None
        L2.tail.next = None
        return L2

    def splice(self, x, L2):
        after = x.next   
        x.next = L2.head
        x.next.prev = x
        
        after.prev = L2.tail        
        after.prev.next = after
        return 