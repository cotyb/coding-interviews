"""
File name   : codes-coding-interviews
Description : implement the codes in coding interviews

Author: cotyb
Change Activity: cotyb establish this file in 1/31 2016
--------------------------------------------------------
"""
#coding=utf-8

import time

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

        print num1



if __name__ == "__main__":
    codes = Codes()
    st = time.time()
    #print codes.four_replace_space("we are happy")
    #codes.A1_insert2_A2([2,5,7,8,0,0,0,0,0,0],[1,3,4,23,56])
    print time.time() - st