class Singly_linked_list:
    """
    Implementation of a singly linked list
    """
    def __init__(self, head_node=None):
        self.head_node = head_node
        
    def list_traversed(self):
        respuesta = ''
        node = self.head_node
        if node:
            respuesta += str(node.val)
            #print(node.val, end = '')
        while node:
            if node != self.head_node:
                respuesta += ' -> '
                respuesta += str(node.val)
                #print(' -> {}'.format(node.val), end = '')
            node = node.next_node
            
        return respuesta
            
    def insert_head(self, new_node):
        # insert to the head
        # A -> B -> null
        # R -> A -> B -> null 
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
        
    def insert_tail(self, new_node):
        # insert to the tail
        # A -> B -> null
        # A -> B -> R -> null 
        node = self.head_node
        prev = None
        while node:
            prev = node
            node = node.next_node
        prev.set_next_node(Node(new_node))
        
    def insert_middle(self, new_node, value):
        # insert in the middle
        # A -> B -> C -> null
        # A -> B -> R -> C -> null
        node = self.head_node
        while node.val != value:
            node = node.next_node
        if node:
            new_node.set_next_node(node.next_node)
            node.set_next_node(new_node)
        else:
            self.insert_tail(new_node)
            
    def delete_head(self):
        if self.head_node.next_node:
            self.head_node = self.head_node.next_node
        else:
            self.head_node = None
    
    def delete_tail(self):
        if self.head_node.next_node:
            prev = self.head_node
            node = prev.next_node
        
            while node.next_node:
                prev = node
                node = node.next_node

        
            prev.next_node = None
        else:
            self.head_node = None
            
    
    def delete_node(self, value):
        prev = self.head_node
        node = prev.next_node
        
        if node:
        
            if prev.val == value:
                self.head_node = self.head_node.next_node
                prev.next_node = None
            
            else:
            
                while node.val != value:
                        prev = node
                        node = node.next_node
                        
                        if node == None:
                            break
                    
                if node:
                    prev.set_next_node(node.next_node)
                    node.next_node = None
                    
                else:
                    print("Valor no se encuentra")
        else:
            self.head_node = None
            
                
    def reverse_list(lista):
            prev = None
            # We start with the head node
            node = lista.head_node

            
            while node:
                next_node = node.next_node
                node.next_node = prev
                prev = node
                node = next_node

            lista.head_node = prev
