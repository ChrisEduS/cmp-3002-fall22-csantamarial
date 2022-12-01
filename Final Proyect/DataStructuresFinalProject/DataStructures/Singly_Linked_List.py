import ctypes

class Node:
    """
    Implementation of a node
    """
    def __init__(self, val=None):
        self.val = val
        self.next_node = None
        
    def set_next_node(self, node):
        self.next_node = node

class Singly_linked_list:
    """
    Implementation of a singly linked list
    """
    def __init__(self, head_node=None):
        self.head_node = head_node
        
    def list_traversed(self):
        respuesta = ''
        node = self.head_node
        respuesta.append(str(node.val))
        #print(node.val, end = '')
        while node:
            if node != self.head_node:
                respuesta.append('->')
                respuesta.append(str(node.val))
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
            
    def delete_node(self, value):
        prev = self.head_node
        node = prev.next_node
        
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
                
    def delete_tail(self):
        prev = self.head_node
        node = prev.next_node
        
        while node.next_node:
            prev = node
            node = node.next_node

        
        prev.next_node = None
