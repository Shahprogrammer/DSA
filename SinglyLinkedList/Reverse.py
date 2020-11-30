"""
    Reverse the SinglyLinkedList

    https://www.geeksforgeeks.org/reverse-a-linked-list/
"""
from SinglyLinkedList import SinglyLinkedList as LinkedList

class SinglyLinkedList(LinkedList):
    def reverse(self)->None:
        prev=None
        current=self.node
        while current != None:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        self.node=prev
        return None
