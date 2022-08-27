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

class Solution:
    def mergeTwoLists(self, list1, list2):
        temp = None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.data <= list2.data:
            temp = list1
            temp.next = self.mergeTwoLists(list1.next, list2)
        else:
            temp = list2
            temp.next = self.mergeTwoLists(list1, list2.next)
        return temp


"""
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""
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

        llist3 = Solution().mergeTwoLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ')
        # fptr.write('\n')
        print("\n", end="")

    # fptr.close()
