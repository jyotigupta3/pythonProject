#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep):
    while node:
        # fptr.write(str(node.data))
        print(str(node.data), end="")
        node = node.next

        if node:
            # fptr.write(sep)
            print(sep, end="")


def mergeLists(head1, head2):
    temp = None
    while head1:
        temp = head1
        head1 = head1.next
        if head1 is not None:
            print("head1", head1.data, temp.data)
        else:
            print("head1 = ", None)

    while head2:
        head1 = head2
        head2 = head2.next
    return head1


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ')
        # fptr.write('\n')
        print("\n", end="")

    # fptr.close()
