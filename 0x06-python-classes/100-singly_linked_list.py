#!/usr/bin/python3
"""Defines a node of a singly linked list"""


class Node:
    """
    Defines a class called Node that is a node of a linked list.

    Attribute:
        __data (int): The data stored in the node.
        __next_node (Node): The next node in the linked list.
    """
    def __init__(self, data, next_node=None):
        """
        The constructor for the Node class.

        Args:
            data (int): The data to store in the node.
            next_node (Node): The next node in the linked list.

        Raises:
            TypeError: If data is not an integer or if next_node is not None or
            a Node object.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        This method retrieves the value of the __data attribute.

        Returns:
            int: The value of the __data atrribute.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        This method sets the value of the __data attribute.

        Args:
            value (int): The value to set the __data attribute to.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        This method retrieves the value of the __next_node attribute.

        Returns:
            Node: The value of the __next_node attribute.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        This method sets the value of the __next_node attribute.

        Args:
            TypeError: If value is not None or a Node object.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be None or a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a singly linked list.

    Attributes:
        head: The head node of the linked list.
    """
    def __init__(self):
        """
        The constructor for the SinglyLinkedList class.

        Initializes an empty linked list with a None head.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list
        (incrementing order).

        Args:
            value (int): The data to store in the new node.

        Raises:
            TypeError: If value is not an integer.

        Returns:
            None
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if new_node.data < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and \
                current.next_node.data < new_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of all nodes in this linked list.
        Each node's data will be printed on a new line.
        """
        result = ""
        current = self.head

        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node

        return result[:-1]
