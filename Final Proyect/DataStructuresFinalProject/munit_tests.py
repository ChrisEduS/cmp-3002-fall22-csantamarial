# Faltaría importar 'Stack_Modified'
from DataStructures import Array, Doubly_Linked_List, Singly_Linked_List, Queue, Priority_Queue, Stacks, FactorialRecursion,FactorialMemoization, 
FibonacciRecursion,FibonacciMemoization

from FactorialRecursion import factorial
from FactorialMemoization import factorial
from FibonacciRecursion import factorial
from FibonacciMemoization import factorial

import unittest
import hypothesis.strategies as st
from hypothesis import given
 import math


class TestFactorial(unittest.TestCase):  
    """
    Check that the factorial function raises a "TypeError" if the n entered is 
    a letter
    """
    def test_n_is_letter(self):
        with self.assertRaises(TypeError):
            factorial('one')
    
    """
    Check that the factorial function raises a "TypeError" if the n entered is 
    a float number
    """
    def test_n_is_float(self):
        with self.assertRaises(TypeError):
            factorial(1.1)
            
    """
    Check that the factorial function raises a "ValueError" if the n entered 
    is n<0
    """
    def test_n_less_than_0(self):
        with self.assertRaises(ValueError):
            factorial(-1)
            
    """
    Check that the result of the factorial is '1' if 'n == 0' 
    """
    def test_n_is_0(self):
        self.assertEqual(factorial(0), 1)

    """
    Check that the factorial function was calculated correctly by using the 
    definition that says the factorial of a number divided by the factorial of 
    that number minus one is the original number
    """
    @given(st.integers(min_value=2, max_value=100))
    def test_n_greater_than_0(self,n):
        result = int(factorial(n) / factorial(n - 1))
        self.assertEqual(n, result)
        

class TestFibonacci(unittest.TestCase):  
    """
    Check that the fibonacci function raises a "TypeError" if the n entered is 
    a letter
    """
    def test_n_is_letter(self):
        with self.assertRaises(TypeError):
            fibonacci('one')
    
    """
    Check that the fibonacci function raises a "TypeError" if the n entered is 
    a float number
    """
    def test_n_is_float(self):
        with self.assertRaises(TypeError):
            fibonacci(1.1)
            
    """
    Check that the fibonacci function raises a "ValueError" if the n entered 
    is n<0
    """
    def test_n_less_than_0(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
            
    """
    Check that the result of the fibonacci is '0' if 'n == 0' 
    """
    def test_n_is_0(self):
        self.assertEqual(fibonacci(0), 0)

    """
    Check that the result of the fibonacci is '1' if 'n == 1' 
    """
    def test_n_is_1(self):
        self.assertEqual(fibonacci(1), 1)

    """
    Check that the fibonacci function was calculated correctly by using the Binet’s Formula this is a formula that is 
    used to find the nth term of the Fibonacci sequence
    """
    @given(st.integers(min_value=2, max_value=20))
    def test_n_greater_than_1(self,n):
        result = int(((((1 + math.sqrt(5)) / 2) ** (n))-(((1 - math.sqrt(5)) / 2) ** (n)))/(math.sqrt(5)))
        self.assertEqual(fibonacci(n), result)
       
# ***********************
# *** Juan Diego Vaca ***
# ***********************

"""
Variables para probar 'delete_head'
"""
# *** Lista con 3 elementos
a = Node('A')
L = Singly_linked_list(a)
L.insert_tail('B')
L.insert_tail('C')

# *** Lista con 2 elementos
b = Node('B')
L2 = Singly_linked_list(b)
L2.insert_tail('C')

# *** Lista con 1 elemento
c =  Node('A')
L3 =  Singly_linked_list(c)

# Listas con 0 elementos
L4 =  Singly_linked_list(None)
L5 =  Singly_linked_list()

"""
Variables parra probar 'delete_tail'
"""
# *** Lista con 3 elementos
d =  Node('A')
L6 =  Singly_linked_list(d)
L6.insert_tail('B')
L6.insert_tail('C')

# *** Lista con 2 elementos
e =  Node('A')
L7 =  Singly_linked_list(e)
L7.insert_tail('B')

# *** Lista con 1 elemento
L8 =  Singly_linked_list( Node('A'))

# *** Lista con 0 elementos
L9 =  Singly_linked_list(None)
L10 =  Singly_linked_list()

"""
Variables para probar 'delete_node'
"""
# *** Lista con 3 elementos
f =  Node(1)
L11 =  Singly_linked_list(f)
L11.insert_tail(2)
L11.insert_tail(3)

# *** Lista con 2 elementos
g =  Node(1)
L12 =  Singly_linked_list(g)
L12.insert_tail(3)

# *** Lista con 1 elemento
L13 =  Singly_linked_list( Node(5))

# *** Listas con 0 elementos
L14 =  Singly_linked_list()
L15 =  Singly_linked_list(None)

"""
Variables para probar 'reverse_list'
"""
# *** Lista con 3 elementos
L16 =  Singly_linked_list( Node(1))
L16.insert_tail(2)
L16.insert_tail(3)

# *** Lista con 3 elementos reversed
L17 =  Singly_linked_list( Node(3))
L17.insert_tail(2)
L17.insert_tail(1)

# *** Lista con 1 elemento
L18 =  Singly_linked_list( Node(3))
L19 =  Singly_linked_list( Node(3))


# *** Lista con 0 elementos
L20 =  Singly_linked_list()
L21 =  Singly_linked_list(None)

"""
Variables para probar push & pop (Stack modificado)
"""
# Stack implementado con Queues
S1 =  Stack_Modified(2)


class Test_Singly_Linked_Lists(unittest.TestCase):
    
    def test_delete_head(self):
        # Revisa funcionamiento normal
        L.delete_head()
        self.assertEqual(L.head_node.val, 'B')
        L2.delete_head()
        self.assertEqual(L2.head_node.val, 'C')
        # Revisa funcionamiento para linked list de 1 solo nodo
        L3.delete_head()
        self.assertEqual(L3.head_node, None)
        # Revisa funcionamiento para linked list vacío
        self.assertEqual(L4.head_node, None)
        self.assertEqual(L5.head_node, None)
        
    def test_delete_tail(self):
        # Revisa funcionamiento normal
        L6.delete_tail()
        self.assertEqual(L6.list_traversed(), L7.list_traversed())
        # Revisa funcionamiento para linked list de 1 solo nodo
        L8.delete_tail()
        self.assertEqual(L8.head_node, None)
        # Revisa funcionamiento para linked list vacío
        self.assertEqual(L9.head_node, None)
        self.assertEqual(L10.head_node, None)
        
        
    def test_delete_node(self):
        # Revisa funcionamiento normal
        L11.delete_node(2)
        self.assertEqual(L11.list_traversed(), L12.list_traversed())
        # Revisar funcionamiento para linked list de 1 solo nodo
        L13.delete_node(5)
        self.assertEqual(L13.head_node, None)
        # Revisar funcionamiento para linked list de 0 elementos
        self.assertEqual(L14.head_node, None)
        self.assertEqual(L15.head_node, None)
        
    def test_reverse_list(self):
        # Revisa funcionamiento normal
        L16.reverse_list()
        self.assertEqual(L16.list_traversed(), L17.list_traversed())
        # Revisa funcionamiento para linked list de 1 solo nodo
        L18.reverse_list()
        self.assertEqual(L18.list_traversed(), L19.list_traversed())
        # Revisar funcionamiento para linked list de 0 elementos
        L20.reverse_list()
        self.assertEqual(L20.head_node, None)
        self.assertEqual(L21.head_node, None)
        
class Test_Modified_Stack(unittest.TestCase):
        
    # Implementación de Stack utilizando Linked List
    def test_push_and_pop(self):
        S1.push(Node(2))
        self.assertEqual(S1.top().val, 2)
        S1.push(Node(0))
        self.assertEqual(S1.top().val, 0)

if __name__ == '__main__':
    unittest.main()
