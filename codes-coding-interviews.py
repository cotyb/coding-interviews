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
import copy
import heapq


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


class DoubleListNode():
    def __init__(self, x):
        self.val = x
        self.prior = None
        self.next = None

class ComplexListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
        self.sibling = None


class BinaryTreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Min_Stack():
    def __init__(self):
        self.data_stack = Queue.LifoQueue()
        self.min_stack = Queue.LifoQueue()

    def min_get_min(self):
        if not self.data_stack.empty() and not self.min_stack.empty():
            return self.min_stack.get()

    def min_push(self, x):
        self.data_stack.put(x)
        if self.min_stack.empty():
            self.min_stack.put(x)
        else:
            now_min = self.min_stack.get()
            self.min_stack.put(now_min)
            if x <= now_min:
                self.min_stack.put(x)
            else:
                self.min_stack.put(now_min)

    def min_pop(self):
        if not self.data_stack.empty() and not self.min_stack.empty():
            self.min_stack.get()
            return self.data_stack.get()


# min_stack = Min_Stack()
# min_stack.min_push(3)
# min_stack.min_push(4)
# min_stack.min_push(2)
# min_stack.min_push(1)
# min_stack.min_pop()
# print min_stack.min_get_min()
# print min_stack.min_get_min()
# print min_stack.min_get_min()



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

    # p134
    def is_list1_the_pop_order_of_list2(self, list1, list2):
        if not list1 and not list2:
            return True
        elif not list1 or not list2:
            return False
        length1 = len(list1)
        length2 = len(list2)
        assert length1 == length2
        stack1 = Queue.LifoQueue()
        index1, index2 = 0, 0
        res = False
        while index2 < length2:
            while stack1.empty() or self.pop_without_del(stack1) != list2[index2]:
                if index1 == length1:
                    break
                stack1.put(list1[index1])
                index1 += 1
            if self.pop_without_del(stack1) != list2[index2]:
                break
            stack1.get()
            index2 += 1

        if stack1.empty() and index2 == length2:
            res = True
        return res

    def pop_without_del(self, stack):
        if stack.empty():
            return
        top = stack.get()
        stack.put(top)
        return top

    # p137
    def print_tree_from_top(self, root):
        if not root:
            return []
        queue = Queue.Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
            print node.val

    # p140
    def is_postorder_of_search_tree(self, list):
        if not list or len(list) == 1:
            return True
        root = list[-1]
        left = []
        right = []
        index = 0
        while list[index] < root:
            left.append(list[index])
            index += 1
        right = list[index:-1]
        for ele in right:
            if ele < root:
                return False
        return self.is_postorder_of_search_tree(left) and self.is_postorder_of_search_tree(right)

    # p143
    def find_path(self, root, target):
        if not root:
            return None
        result = []
        self.find_path_recursive(root, target, [], result)
        return result

    def find_path_recursive(self, root, target, path, result):
        if not root.right and not root.left and target == root.val:
            path.append(root.val)
            result.append(path)
        if root.left:
            self.find_path_recursive(root.left, target-root.val, path+[root.val], result)
        if root.right:
            self.find_path_recursive(root.right, target-root.val, path+[root.val], result)
        return result

    # p147
    def complex_linkedlist_clone(self, head):
        '''
        three steps:
        first: copy every node and bind them
        second: sibling
        third: divide the linked list into two
        '''
        head = self.clone_nodes(head)
        head = self.connect_sibling_nodes(head)
        clone_head = self.reconnect_nodes(head)
        return head, clone_head


    def clone_nodes(self, head):
        res = head
        if not head:
            return None
        while head.next:
            tmp = ComplexListNode(head.val)
            tmp.next = head.next
            head.next = tmp
            head = tmp.next
        tmp = ComplexListNode(head.val)
        head.next = tmp
        return res

    def connect_sibling_nodes(self, head):
        if not head:
            return None
        res = head
        while head:
            if head.sibling:
                head.next.sibling = head.sibling.next
            head = head.next.next
        return res

    def reconnect_nodes(self, head):
        if not head:
            return None
        clone_head = head.next
        clone_result = clone_head
        head.next = clone_head.next
        head = head.next
        while head:
            clone_head.next = head.next
            clone_head = clone_head.next
            head.next = clone_head.next
            head = head.next
        return clone_result

    # p151
    def covert_binary_tree2linkedlist(self, root):
        if not root:
            return None
        last_node = [None]
        self.covert(root, last_node)
        head = last_node[0]
        while head.left:
            head = head.left
        return head


    def covert(self, root, last_node):
        if not root:
            return
        current = root
        if root.left:
            self.covert(root.left, last_node)
        current.left = last_node[0]
        if last_node[0]:
            last_node[0].right = current
        last_node[0] = current
        if root.right:
            self.covert(root.right, last_node)

    # p154 28
    def permutation(self, str):
        res = []
        if len(str) <= 1:
            return str
        for i in range(len(str)):
            tmp = str[:i] + str[i+1:]
            for ele in self.permutation(tmp):
                res.append(str[i]+ele)

        return res

    # p163 29
    def more_than_half_num_simple(self, alist):
        if not alist:
            return
        cnt = 0
        current = alist[0]
        for ele in alist[1:]:
            if ele == current:
                cnt += 1
            else:
                if cnt != 0:
                    cnt -= 1
                else:
                    current = ele
        if alist.count(current) > len(alist) / 2:
            return current

    def more_than_half_num_recursive(self, alist):
        if not alist:
            return
        length = len(alist)
        start = 0
        end = length - 1
        mid = length / 2
        index = self.partition_quick(alist, length, start, end)
        while index != mid:
            if index > mid:
                end = index - 1
                index = self.partition_quick(alist, length, start, end)
            else:
                start = index + 1
                index = self.partition_quick(alist, length, start, end)
        if alist.count(alist[mid]) > length / 2:
            return alist[mid]

    def partition_quick(self, alist, length, start, end):
        base = alist[start]
        #index = 0
        index1, index2 = start, end
        while index1 < index2:
            while index1 < index2 and alist[index2] >= base:
                index2 -= 1
            alist[index1] = alist[index2]
            while index1 < index2 and alist[index1] <= base:
                index1 += 1
            alist[index2] = alist[index1]
        alist[index1] = base
        return index1

    # p167 30
    def get_least_numbers(self, alist, k):
        if not alist or k <= 0:
            return
        length = len(alist)
        if k > length:
            return
        start, end = 0, length - 1
        index = self.partition_quick(alist, length, start, end)
        while k != index:
            if index > k:
                end = index - 1
                index = self.partition_quick(alist, length, start, end)
            else:
                start = index + 1
                index = self.partition_quick(alist, length, start, end)
        return alist[:index]

    def get_least_numbers_big_data(self, alist, k):
        max_heap = []
        length = len(alist)
        if not alist or k <= 0 or k > length:
            return
        k = k - 1
        for ele in alist:
            ele = -ele
            if len(max_heap) <= k:
                heapq.heappush(max_heap, ele)
            else:
                heapq.heappushpop(max_heap, ele)

        return map(lambda x:-x, max_heap)

    # p171 31
    def find_great_sum_of_subarray(self, alist):
        length = len(alist)
        max_sum = alist[0]
        if not alist:
            return
        tmp_sum = 0
        for ele in alist:
            if tmp_sum <= 0:
                tmp_sum = ele
            else:
                tmp_sum += ele
            if tmp_sum > max_sum:
                max_sum = tmp_sum


        return max_sum

    # p174 32
    def number_of_1_between_1_and_n(self, n):
        if n <= 0:
            return 0
        num_str = str(n)
        length = len(num_str)
        return self.number_of_1(num_str, length)

    def number_of_1(self, string, length):
        if not string:
            return 0
        first = string[0]
        if length == 1 and first == '0':
            return 0
        if length == 1 and first > '0':
            return 1
        numfisrtdigit = 0
        first = ord(first) - ord('0')
        if first > 1:
            numfisrtdigit = pow(10, length - 1)
        elif first == 1:
            numfisrtdigit = int(string[1:]) + 1

        numotherdigits = first * (length - 1) * pow(10, length - 2)
        numrecursive = self.number_of_1(string[1:], length - 1)

        return numfisrtdigit + numotherdigits + numrecursive

    # p177 33
    def get_min_number(num_list):
        pass

    # p182 34
    def ugly_num(self, n):
        if n < 1:
            return 0
        index = 0
        num = 0
        while index < n:
            num += 1
            if self.is_ugly_num(num):
                index += 1
        return num

    def is_ugly_num(self, num):
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        if num == 1:
            return True
        return False

    def ugly_replace_time_with_space(self, n):
        result = [1]
        if n < 1:
            return 0
        index_2 = 0
        index_3 = 0
        index_5 = 0
        while len(result) < n:
            result.append(min(result[index_2] * 2, result[index_3] * 3, result[index_5] * 5))
            while result[index_2] * 2 <= result[-1]:
                index_2 += 1
            while result[index_3] * 3 <= result[-1]:
                index_3 += 1
            while result[index_5] * 5 <= result[-1]:
                index_5 += 1
        return result[-1]









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
    head1.next = a
    a.next = b
    b.next = c
    head2.next = d
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
    root1 = BinaryTreeNode(10)
    a = BinaryTreeNode(6)
    b = BinaryTreeNode(14)
    c = BinaryTreeNode(4)
    d = BinaryTreeNode(8)
    e = BinaryTreeNode(12)
    f = BinaryTreeNode(16)
    root2 = BinaryTreeNode(8)
    g = BinaryTreeNode(9)
    h = BinaryTreeNode(2)
    root2.left = g
    root2.right = h
    root1.left = a
    root1.right = b
    a.left = c
    a.right = d
    b.left = e
    b.right = f
    a = ComplexListNode(1)
    b = ComplexListNode(2)
    c = ComplexListNode(3)
    d = ComplexListNode(4)
    e = ComplexListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    a.sibling = c
    b.sibling = e
    d.sibling = b
    #print codes.mirror_binary_tree(root1)
    #codes.print_matrix_clockwise([[1,2,3],[5,6,7],[8,9,10]])
    # print codes.is_list1_the_pop_order_of_list2([3],[3])
    # codes.print_tree_from_top(root1)
    # print codes.is_postorder_of_search_tree([50,7,6,9,11,10,8])
    # print codes.find_path(root1, 22)
    # head, clone_head = codes.complex_linkedlist_clone(a)
    # head1 = head1.next
    # head = codes.covert_binary_tree2linkedlist(root1)
    # print codes.permutation("abc")
    #print codes.more_than_half_num_simple([2,2,2,2,1,2,4,2,1,1,2,1])
    #print codes.get_least_numbers_big_data([4,5,1,6,2,7,3,8], 9)
    #print codes.find_great_sum_of_subarray([-1,-2,-3,-10,-4,-7,-2,-5,-22])
    #print codes.number_of_1_between_1_and_n()
    #print codes.ugly_num(1500)
    print codes.ugly_replace_time_with_space(1500)










    print time.time() - st