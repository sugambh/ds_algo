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

    def delete(self, data):
        if self.head is not None:
            if self.head.data == data:
                self.head = self.head.next
            else:
                previous = None
                current = self.head
                while current is not None and current.data != data and current.next is not None:
                    previous = current
                    current = current.next
                if current.data == data and current.next is None:
                    previous.next = None
                elif current.data == data and current.next is not None:
                    previous.next = current.next
                    current.next = None
                else:
                    print("no such node found")
        else:
            print("empty list")

    def search(self, data):
        found = False
        current = self.head
        while current:
            if current.data == data:
                found = True
                break
            else:
                current = current.next
        if found:
            print(str(data) + " is present ")
        else:
            print(str(data) + " not present ")

    def size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size

    def recursive_reverse(self, node):
        current = node
        if current is None:
            return None
        if current.next is None:
            self.head = current
            return current
        temp = self.recursive_reverse(current.next)
        temp.next = current
        current.next = None
        return current

    def iterative_reverse(self):
        first = self.head
        if first is None:
            print("empty list")
        else:
            second = first.next
            first.next=None
            while (first is not None and second is not None):
                temp1 = second
                temp2 = second.next
                second.next = first
                first = temp1
                second = temp2
            self.head = first
