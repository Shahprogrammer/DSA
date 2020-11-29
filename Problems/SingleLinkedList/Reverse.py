"""
    Reverse the SingleLinkedList

    https://www.geeksforgeeks.org/reverse-a-linked-list/
"""
import sys,pathlib
sys.path.insert(1, str(pathlib.Path(__file__).resolve().parent.parent.parent))
from Implementation.SinglyLinkedList import SinglyLinkedList as LinkedList

class SinglyLinkedList(LinkedList):
    def reverse(self)->LinkedList:
        prev=None
        current=self.node
        while current != None:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        self.node=prev
        return None
