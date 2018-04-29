# Written by Karan Kaushik for COMP9021
# =============================================================================
# Generates a linked list of an even length of 4 or more, 
# determined by user input, and reorders the list so that it 
# starts with the first occurrence of the smallest element and 
# repeatively moves backwards by one step and forward by three steps, wrapping around when needed.
# =============================================================================


from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def insert_value_move_head(self, new, node):
        new.value = node.next_node.value
        node.next_node.value = None

    
    def check_all_none(self):
        

        node = self.head
        
        while node:
            
            if node.value is not None:
                return False
            node = node.next_node  
        
        return True
            
    def rearrange(self):
        
        minimum_element = 99999999
        node = self.head
        index = 0
        
        ##find minimum element
        while node:
            if node.value < minimum_element:
                minimum_element = node.value
                index = self.index_of_value(node.value)
            node = node.next_node
        
        L = self.duplicate()
        new = L.head
        node = self.head
        
        while True:
            if not node:
                    node = self.head
            if node.value != minimum_element:
                node = node.next_node        
            else:
                break
        
        ##put minimumelement at the head
        L.head.value = node.value
        node.value = None
        
        
        #find out if whether to go one step back or two steps forward
        iterator = 0
        
        
        ##while our linkedlist is not all none. element is none if it is added to the other list. 
        while not self.check_all_none():
            
            node = self.head
            if iterator % 2 == 0:
                index = index - 1
                if index < 0:
                    index = len(self) - 1
            else:
                
                index = (index + 3) % len(self)
            
            for _ in range(index):
                
                node = node.next_node
                if not node:
                    node = self.head
                
                        
                   
            new = new.next_node
            new.value = node.value
            node.value = None
            iterator += 1
             
            
        
           
        new = L.head
        current = self.head
        #copy over values from new list to original list
        for _ in range(len(self)):
            current.value = new.value
            current = current.next_node
            new = new.next_node
        
        
        
    
