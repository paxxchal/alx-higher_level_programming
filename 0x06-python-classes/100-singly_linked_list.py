#!/usr/bin/python3
"""This module defines a Node class
and a SinglyLinkedList class for a singly linked list."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
        - data: Data to be stored in the node (must be an integer).
        - next_node (Node): Next node in the linked list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data.

        Args:
        - value: Data value to be set (must be an integer).

        Raises:
        - TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next_node.

        Args:
        - value: Next node in the linked list (must be a Node or None).

        Raises:
        - TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes a new instance
        of the SinglyLinkedList class with an empty list."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the
        correct sorted position in the list (increasing order).

        Args:
        - value: Data value for the new Node (must be an integer).
        """
        new_node = Node(value)

        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Prints the entire list in stdout, one node number by line."""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip("\n")
