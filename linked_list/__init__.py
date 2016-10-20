from __future__ import print_function


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current is not None:
            if current.next is None:
                print(str(current.data) + "-#", end='')
            else:
                print(str(current.data) + "->", end='')
            current = current.next

    def delete(self,data):
        if self.head is not None:
            if self.head.data == data:
                self.head = self.head.next
            else:
                previous = None
                current = self.head
                while current is not None and current.data!=data and current.next is not None:
                    previous = current
                    current = current.next
                if current.data == data and current.next is None:
                    previous.next=None
                elif current.data == data and current.next is not None:
                    previous.next = current.next
                    current.next=None
                else:
                    print ("no such node found")


        else:
            print ("empty list")
