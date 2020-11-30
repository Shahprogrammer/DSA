import sys,pathlib
sys.path.insert(1, str(pathlib.Path(__file__).resolve().parent.parent.parent))
from Problems.SinglyLinkedList.Reverse import SinglyLinkedList as LinkedList
"""
    Reverse a Linked List in groups of given size.

    https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1
"""
class SinglyLinkedList(LinkedList):
    def combine(self,data):
        self.get_last_node().next=data
        return None
    def get_n(self, head,n:int):
        i=0
        node=head
        temp=SinglyLinkedList()
        while node != None and i<n:
            temp.append(node.data)
            node=node.next
            i+=1
        temp.reverse()
        if node != None:
            next=self.get_n(node,n)
            temp.combine(next.node)
        return temp
    def reverseN(self,n:int) -> None:
        data=self.get_n(self.node,n)
        self.node=data.node
        return None
