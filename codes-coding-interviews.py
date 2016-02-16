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
import gc


class Queue_With_Two_Stacks():
    '''
    implement queue with two stacks
    '''

    def __init__(self):
        self.stackin = Queue.LifoQueue()
        self.stackout = Queue.LifoQueue()

    def appendTail(self, num):
        '''
        insert the num into the end of the queue
        :param num: int, the element to insert
        :return: noting
        '''
        if self.stackin.full() and self.stackout.full():
            print "the queue is full"
            return
        if not self.stackin.full():
            self.stackin.put(num)
            return
        while not self.stackin.empty():
            self.stackout.put(self.stackin.get())
        self.stackin.put(num)


    def deleteHead(self):
        '''
        delete the element in the head of the queue
        :return: noting
        '''
        if self.stackin.empty() and self.stackout.empty():
            print "the queue is empty"
            return
        if not self.stackout.empty():
            self.stackout.get()
            return
        while not self.stackin.empty():
            self.stackout.put(self.stackin.get())
        self.stackout.get()


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

    def age_sort(self, age_list):
        '''
        sort the age of employees of a company
        suppose the age range from 0 to 100
        :param age_list: a list of age num
        :return: sorted list
        '''
        age_count = {}
        result = []
        if None == age_list:
            return
        for age in age_list:
            if age < 0 or age > 100:
                print "%s the age is out of bound" %age
                continue
            age_count[age] = age_count.get(age, 0) + 1

        for age in range(0, 101):
            result += age_count.get(age, 0) * [age]

        return result

    def find_min_of_rotated_list(self, rotated_list):
        '''
        p66, implement this question with recursive
        :param rotated_list: a rotated list
        :return: the min num
        '''
        if [] == rotated_list:
            return
        #start, end = 0, len(rotated_list) - 1
        return self.partition(rotated_list)

    def partition(self, rotated_list):
        start, end = 0, len(rotated_list) - 1
        if rotated_list[-1] > rotated_list[0]:
            return rotated_list[0]
        if len(rotated_list) == 1:
            return rotated_list[0]
        mid = (start + end) / 2
        if rotated_list[mid] == rotated_list[start] and rotated_list[start] == rotated_list[end]:
            return self.find_min_in_order(rotated_list)
        elif rotated_list[mid] >= rotated_list[start]:
            return self.partition(rotated_list[mid+1:])
        else:
            return self.partition(rotated_list[:mid+1])

    def find_min_rotated_list_loop(self, rotated_list):
        '''
        p66 implement this question with loop
        :param rotated_list: a rotated list
        :return: the min num
        '''
        if [] == rotated_list:
            return
        end = len(rotated_list) - 1
        start = 0
        mid = start
        while rotated_list[start] >= rotated_list[end]:
            if end - start == 1:
                mid = end
                break
            mid = (start + end) / 2
            if rotated_list[mid] == rotated_list[start] and rotated_list[start] == rotated_list[end]:
                return self.find_min_in_order(rotated_list[start:end+1])
            elif rotated_list[mid] >= rotated_list[start]:
                start = mid
            else:
                end = mid
        return rotated_list[mid]

    def find_min_in_order(self, rotated_list):
        '''
        :param rotated_list: a list that
        :return: the min num
        '''
        result = rotated_list[0]
        for ele in rotated_list:
            if ele < result:
                result = ele
        return result

    def fibonacci_recursive(self, n):
        '''
        print the nth fibonacci num with recursive
        :param n: the nth number
        :return: the num
        '''
        if n < 0:
            print "your input is error"
            return
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fibonacci_recursive(n-1) + self.fibonacci_recursive(n-2)

    def fibonacci_loop(self, n):
        '''
        print the nth fibonacci num with loop
        :param n:
        :return:
        '''
        if n < 0:
            print "your input is error"
            return
        if n == 1:
            return 1
        if n == 0:
            return 0
        a, b = 0, 1
        i = 2
        while i <= n:
            c = a + b
            a,b = b, c
            i += 1
        return c

    def num_of_one(self, n):
        '''
        count the num of one in num n
        bin():convert the num to binary string
        :param n: num n
        :return: the num of one in n
        '''
        if n >= 0:
            nbin = bin(n)
            return nbin.count('1')
        else:
            n = abs(n)
            nbin = bin(n-1)
            return 32 - nbin.count('1')

    def power(self, base, exponent):
        '''
        compuate the exponent power of base
        :param base:
        :param exponent:
        :return: the power
        '''
        if self.equal(base, 0.0) and exponent < 0:
            print "your input is invalid"
            return
        absexponent = abs(exponent)
        result = self.compute_power_recursive(base, absexponent)
        if exponent < 0:
            result = 1.0 / result
        return result

    def compute_power_recursive(self, base, exponent):
        '''
        compute the power recursive
        :param base:
        :param exponent:
        :return: the power
        '''
        if exponent == 1:
            return base
        if exponent == 0:
            return 1
        if exponent % 2 == 0:
            tmp = self.power(base, exponent >> 1)
            return tmp * tmp
        if exponent % 2 == 1:
            tmp = self.power(base, exponent >> 1)
            return tmp * tmp * base

    def equal(self, num1, num2):
        if abs(num1 - num2 ) < 0.0000001:
            return True
        return False

    def print_form_one_to_n(self, n):
        num, i = 1, 0
        while i < n:
            num = num * 10
            i += 1
        for ele in range(1, num):
            print ele

    def print_1_to_max_of_n_digits(self, n):
        if n < 0:
            return
        res = "1"
        while len(res) <= n:
            print res
            res = self.str_plus_one(res)
            if res == -1:
                print "error"
                break


    def str_plus_one(self, str):
        c = 0
        res = ""
        if str == "":
            return "1"
        if ord(str[-1]) < ord('0') and ord(str[-1]) > ord('9'):
            print "error"
            return -1
        if ord(str[-1]) >= ord('0') and ord(str[-1]) < ord('9'):
            return str[:-1] + chr(ord(str[-1]) + 1)
        if ord(str[-1]) == ord('9'):
            res = self.str_plus_one(str[:-1]) + "0"
            return res

    def print_1_to_max_n_digits_recursive(self, n):
        if n < 0:
            return
        if n == 0:
            return ''
        for i in range(10):
            res = chr(ord('0') + i)
            self.print_1_to_max_n_digits_recursively(res, 0, n)

    def print_1_to_max_n_digits_recursively(self, res, n, length):
        if n == length - 1:
            print res.lstrip('0')
            return
        for i in range(10):
            self.print_1_to_max_n_digits_recursively(res + chr(ord('0') + i), n+1, length)

    def delete_node_of_list(self, head, delete):
        if not head or not delete:
            return
        if delete.next != None:
            next_node = delete.next
            delete.val = next_node.val
            delete.next = next_node.next
        elif head == delete:
            return -1
        else:
            tmp = head
            while tmp.next != delete:
                tmp = tmp.next
            tmp.next = None

    def odd_before_even(self, mixed_list):
        if mixed_list == []:
            return
        index1 = 0
        index2 = len(mixed_list) - 1
        while index1 < index2:
            while mixed_list[index2] & 0x1 != 1 and index1 < index2:
                index2 -= 1
            while mixed_list[index1] & 0x1 == 1 and index1 < index2:
                index1 += 1
            mixed_list[index1], mixed_list[index2] = mixed_list[index2], mixed_list[index1]
        return mixed_list

    def find_kth_to_tail(self, head, k):
        if not head:
            return None
        if k <= 0:
            return None
        index1 = 1
        res = head
        tmp = head
        while tmp.next and index1 < k:
            tmp = tmp.next
            index1 += 1
        if index1 != k:
            print "k is larger than the length of the list"
            return
        while tmp.next:
            tmp = tmp.next
            res = res.next
        return res.val

    #p112
    def reverse_linkedlist(self, head):
        if not head:
            return
        before_node = None
        while head.next:
            after_node = head.next
            head.next = before_node
            before_node = head
            head = after_node
        head.next = before_node
        return head

    #p114
    def merge_sorted_linkedlist(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        if head1.val <= head2.val:
            head1.next = self.merge_sorted_linkedlist(head1.next, head2)
            return head1
        else:
            head2.next = self.merge_sorted_linkedlist(head1, head2.next)
            return head2

    #p117
    def has_sub_tree(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        res = False
        if root1.val == root2.val:
            res = self.does_tree1_have_tree2(root1, root2)
        if not res and root1.left:
            res = self.has_sub_tree(root1.left, root2)
        if not res and root1.right:
            res = self.has_sub_tree(root2.right, root2)
        return res

    def does_tree1_have_tree2(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        return self.does_tree1_have_tree2(root1.left, root2.left) and self.does_tree1_have_tree2(root1.right, root2.right)

    #p125
    def mirror_binary_tree(self, root):
        if not root:
            return
        if not root.left and not root.right:
            return
        root.left, root.right = root.right, root.left
        self.mirror_binary_tree(root.right)
        self.mirror_binary_tree(root.left)

    #p127
    def print_matrix_clockwise(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        if row == 0 and col == 0:
            return
        start = 0
        while row > 2 * start and col > 2 * start:
            self.print_rec(matrix, row, col, start)
            start += 1

    def print_rec(self, matrix, row, col, start):
        end_x = col - 1 - start
        end_y = row - 1 - start
        x = start
        while x <= end_x:
            print matrix[start][x]
            x += 1
        if start < end_y:
            x = start + 1
            while x <= end_y:
                print matrix[x][end_x]
                x += 1
        if start < end_x and start < end_y:
            x = end_x - 1
            while start <= x:
                print matrix[end_y][x]
                x -= 1
        if start < end_y - 1 and start < end_x:
            x = end_y - 1
            while start < x:
                print matrix[x][start]
                x -= 1







if __name__ == "__main__":
    codes = Codes()
    st = time.time()
    #print codes.four_replace_space("we are happy")
    #codes.A1_insert2_A2([2,5,7,8,0,0,0,0,0,0],[1,3,4,23,56])
    # a = ListNode(1)
    # b = ListNode(2)
    # c = ListNode(3)
    # a.next = b
    # b.next = c
    #codes.reversed_print_linked(a)
    #codes.reversed_link_recursion(a)
    #root = codes.reconstruct_binary_tree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
    #print root.left.left.right.val
    '''
    queue = Queue_With_Two_Stacks()
    for ele in range(10):
        print ele
        queue.appendTail(ele)
    print "hh"
    for i in range(10):
        print queue.deleteHead()
    print codes.age_sort([232,4,3,54,765,42,-1,43,53,34,34,34,43,243,321,24,65,768,98,34,87,34,2,389,7])
    '''
    # for i in range(10):
    #     list = [num for num in range(i)]
    #     for j in range(i):
    #         list = list[j:] + list[:j]
    #         print list
    #         print codes.find_min_of_rotated_list(list)
    # print codes.find_min_rotated_list_loop([1,0,1,1,1])
    # print codes.fibonacci_loop(100)
    #print codes.num_of_one(-1)
    #print codes.power(0,-1)
    #codes.print_1_to_max_of_n_digits(3)
    #codes.print_1_to_max_n_digits_recursive(3)
    head1 = ListNode(1)
    a = ListNode(3)
    b = ListNode(5)
    c = ListNode(7)
    head2 = ListNode(1)
    d = ListNode(4)
    e = ListNode(6)
    f = ListNode(8)
    #head1.next = a
    a.next = b
    b.next = c
    #head2.next = d
    d.next = e
    e.next = f

    #print codes.find_kth_to_tail(head, 43)
    # head = codes.merge_sorted_linkedlist(head1, head2)
    # for i in range(2):
    #     print head.val
    #     head = head.next
    # res = codes.delete_node_of_list(head, head)
    # if res == -1:
    #     head = None
    #print codes.odd_before_even([2,1,12,21,2,321,312,3,213,21,3,213,12,3,12,3,21,3,24,3,5,6,65,767,8,678,8,7,90,89,6,7,4363,25,21,4,3])
    root1 = BinaryTreeNode(8)
    a = BinaryTreeNode(8)
    b = BinaryTreeNode(7)
    c = BinaryTreeNode(9)
    d = BinaryTreeNode(2)
    e = BinaryTreeNode(4)
    f = BinaryTreeNode(7)
    root2 = BinaryTreeNode(8)
    g = BinaryTreeNode(9)
    h = BinaryTreeNode(2)
    root2.left = g
    root2.right = h
    root1.left = a
    root1.right = b
    a.left = c
    a.right = d
    d.left = e
    d.right = f
    #print codes.mirror_binary_tree(root1)
    codes.print_matrix_clockwise([[1,2,3],[5,6,7],[8,9,10]])










    print time.time() - st