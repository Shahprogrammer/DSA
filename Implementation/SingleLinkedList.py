from typing import Any, Union


class Node():
    """
    Node for Single Linked List

    """

    def __init__(self, data: Any, next: Union['Node', None] = None) -> None:
        """
        Generates a Node for Single Linked List

        :param data: Value of the current node of Single Linked List
        :type data: Any
        :param next: Next Node of Single Linked List
        :type next: Union[Node,None]
        """
        self._data = data
        self._next = next

    @property
    def data(self) -> Any:
        """
        Getter Method for data attribute

        :return: self.data
        :rtype: Any
        """
        return self._data

    @data.setter
    def data(self, data: Any):
        """
        Setter Method for data attribute

        :param data: Value to be set for data attribute
        :type data: Any
        """
        self._data = data

    @property
    def next(self) -> Union['Node', None]:
        """
        Getter Method for next attribute

        :return: self.next
        :rtype: Union['Node',None]
        """
        return self._next

    @next.setter
    def next(self, next: Union['Node', None]):
        """
        Setter Method for next attribute

        :param next: Value to be set for next attribute
        :type next: Union['Node',None]
        """
        self._next = next


class SingleLinkedList():
    """
    Generates a Single Linked List

    """

    def __init__(self, node: Union[Node, None] = None):
        """
        Generates a Single Linked List

        :param node: Node of the Single Linked List
        :type node: Union[Node,None]
        """
        self.node = node

    def get_node(self, index) -> Union[Node, None]:
        node = self.node
        for i in range(0, index):
            if node.next != None:
                node = node.next
            else:
                node = None
                break
        return node

    def get_last_node(self) -> Node:
        node = self.node
        if node != None:
            while node.next != None:
                node = node.next
            return node
        else:
            return node

    def append(self, data):
        node = self.get_last_node()
        if node != None:
            node.next = Node(data=data)
        else:
            self.node = Node(data=data)
        return None

    def add(self, data, index):
        node = self.get_node(index-1)
        node.next = Node(data=data, next=node.next)
