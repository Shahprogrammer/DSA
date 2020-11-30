from SinglyLinkedList import SinglyLinkedList as LinkedList
"""
    Check weather Singly Linked List is in loop

    https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/
"""
class SinglyLinkedList(LinkedList):
    def check_loop(self):
        nodes=[]
        node=self.node
        while(node):
            if node not in nodes:
                nodes.append(node)
            else:
                return True
            node=node.next
        return False