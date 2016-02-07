"""
File name   : codes-coding-interviews
Description : implement the codes in coding interviews

Author: cotyb
Change Activity: cotyb establish this file in 1/31 2016
--------------------------------------------------------
"""
#coding=utf-8

import time
import Queue

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class BinaryTreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codes():
    def __init__(self):
        self.__author__ = "cotyb"

    def four_replace_space(self, str):
        '''
        replace space with "%20"
        :param str: str, the string to be replaced
        :return: str, replaced string
        '''
        return str.replace(" ", "%20")

    def A1_insert2_A2(self, num1, num2):
        '''
        insert num2 to num1 in order
        :param num1: list, ordered num list
        :param num2: list, ordered num list
        :return: list, ordered num list composed of num1 and num2
        '''
        if not num1 or not num2:
            return num1 + num2
        num = []
        #len1 = len(num1) - 1
        len1 = 4
        len2 = len(num2)
        len_ = len1 + len2
        while len1 > 0 and len2 > 0:
            if num2[len2-1] >= num1[len1-1]:
                num1[len_-1] = num2[len2-1]
                len_ -= 1
                len2 -= 1
            else:
                num1[len_-1] = num1[len1-1]
                len_ -= 1
                len1 -= 1
        if len1 == 0:
            num1[:len2] = num2[:len2]

    def reversed_print_linked(self, head):
        '''
        print the linked list with reversed order
        :param head: Listnode, the head of the linked list
        :return: the reversed list of value
        '''
        stack = Queue.LifoQueue()
        if not head:
            return
        while head:
            stack.put(head.val)
            head = head.next
        while not stack.empty():
            print stack.get()

    def reversed_link_recursion(self, head):
        '''
        reverse the linked list with recursion
        :param head: the head of the linked list
        :return: noting
        '''
        if not head:
            return
        else:
            self.reversed_link_recursion(head.next)
            print head.val

    def reconstruct_binary_tree(self, prelist, inlist):
        '''
        given the pre-order traversal list and in-order traversal list, construct the binary tree
        :param prelist: the result list of pre-order traversal
        :param inlist:  the result list of in-order traversal
        :return: binary tree
        '''
        if not prelist or not inlist:
            return None
        if len(prelist) != len(inlist):
            print "your input is error"
            return
        if len(prelist) == 1:
            root = BinaryTreeNode(prelist[0])
            return root
        root = BinaryTreeNode(prelist[0])
        index_root_inlist = inlist.index(prelist[0])
        inlist_left = inlist[:index_root_inlist]
        inlist_right = inlist[index_root_inlist+1:]
        left_len, right_len = len(inlist_left), len(inlist_right)
        prelist_left = prelist[1:left_len+1]
        prelist_right = prelist[right_len:]
        root.left = self.reconstruct_binary_tree(prelist_left, inlist_left)
        root.right = self.reconstruct_binary_tree(prelist_right, inlist_right)
        return root




if __name__ == "__main__":
    codes = Codes()
    st = time.time()
    #print codes.four_replace_space("we are happy")
    #codes.A1_insert2_A2([2,5,7,8,0,0,0,0,0,0],[1,3,4,23,56])
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    #codes.reversed_print_linked(a)
    #codes.reversed_link_recursion(a)
    root = codes.reconstruct_binary_tree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
    print root.left.left.right.val


    print time.time() - st