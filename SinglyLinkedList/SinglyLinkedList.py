from typing import Any, Union


class Node():
    """
    Node for Single Linked List

    """

    def __init__(self, data: Any, next: Union['Node', None] = None) -> None:
        """
        Generates a Node for Single Linked List

        :param data: Value of the current node of Singly Linked List
        :type data: Any
        :param next: Next Node of Singly Linked List
        :type next: Union[Node,None]
        """
        self._data = data
        self._next = next

    def __repr__(self) -> str:
        return '<%s %r>' % (self.__class__.__name__, self.data)

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


class SinglyLinkedList():
    """
    Generates a Single Linked List

    """

    def __init__(self, node: Union[Node, None] = None):
        """
        Generates a Singly Linked List

        :param node: Node of the Singly Linked List
        :type node: Union[Node,None]
        """
        self.node = node

    def __repr__(self) -> str:
        return '<%s %r>' % (self.__class__.__name__, self._tolist())

    def get_node(self, index) -> Union[Node, None]:
        return self._tolist()[index]

    def get_last_node(self) -> Node:
        return self._tolist()[-1]

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

    def add_start(self, data):
        node = self.get_node(0)
        self.node = Node(data, node)
        return None

    def _tolist(self):
        nodes = []
        node = self.node
        while(node != None):
            nodes.append(node)
            node = node.next
        return [None]if len(nodes)==0 else nodes

    def tolist(self):
        nodes = []
        node = self.node
        while(node != None):
            nodes.append(node.data)
            node = node.next
        return nodes
    def delete(self,index):
        prev_node=self.get_node(index-1)
        prev_node.next=prev_node.next.next
    def pop(self):
        a=self.get_node(-2)
        a.next=None
    def delete_start(self):
        self.node=self.get_node(1)
    @classmethod
    def fromlist(cls,data:list):
        node=cls()
        for i in data:
            node.append(i)
        return node