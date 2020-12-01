from SinglyLinkedList import SinglyLinkedList as LinkedList
"""
    Delete loop if found in Singly Linked List

    https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/
"""

class SinglyLinkedList(LinkedList):
    def detect_loop(self):
        nodes=[]
        node=self.node
        while(node):
            if node not in nodes:
                nodes.append(node)
            else:
                nodes[-1].next=None
                return True
            node=node.next
        return False
    def delete_loop(self):
        return self.detect_loop()