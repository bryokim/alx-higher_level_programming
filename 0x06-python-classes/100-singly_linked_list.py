#!/usr/bin/python3
"""SinglyLinkedList module

Raises:
    TypeError: If the data for new node is not an integer.
    TypeError: If the next_node is not a Node object or None.
"""


class Node:
    """Defines a node for a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a node.

        Args:
            data (int): Data for the node.
            next_node (:obj:`Node`, optional): Next node. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data.

        The setter for this property raises a TypeError if
        the data being provided is not an integer.

        Returns:
            int: Data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node

        The setter method for the next_node raises a TypeError exception
        if the next_node is not a Node object or None.

        Returns:
            Node object: The next_node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked lists."""

    def __init__(self):
        """Initialize a SinglyLinkedList"""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position
        in the list (increasing order).

        Args:
            value (int): Data for the new Node.
        """
        if self.head is None:
            self.head = Node(value)
        else:
            temp = self.head
            while temp is not None and temp.data < value:
                prev = temp
                temp = temp.next_node

            if temp == self.head:
                self.head = Node(value, self.head)
            elif temp is None:
                prev.next_node = Node(value)
            else:
                prev.next_node = Node(value, temp)

    def __str__(self):
        """Prints a string representation of this list."""

        temp = self.head
        while temp.next_node is not None:
            print(f"{temp.data}")
            temp = temp.next_node
        return str(temp.data)
