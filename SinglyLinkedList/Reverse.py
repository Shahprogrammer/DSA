from SinglyLinkedList import SinglyLinkedList as LinkedList
"""
    Reverse the SinglyLinkedList

    https://www.geeksforgeeks.org/reverse-a-linked-list/
"""
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
