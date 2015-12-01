# !/usr/bin/python
__author__ = 'sagar'

'''
A brief report on the program:

Run Command: python solver1.py
Input parameters: none
Expected sample output:

INFO:root:Execution time : 0.424 minutes.
INFO:root:
 ========================= Solution ======================================
INFO:root:Customer Heather ordered Amplifier but received Elephant and lives at North Avenue
INFO:root:Customer Irene ordered Candelabrum but received Banister and lives at Kirkwood Street
INFO:root:Customer George ordered Banister but received Candelabrum and lives at Lake Avenue
INFO:root:Customer Frank ordered Elephant but received Doorknob and lives at Orange Drive
INFO:root:Customer Jerry ordered Doorknob but received Amplifier and lives at Maxwell Street
INFO:root:
 ========================= End ===========================================

Algorithm: Brute Force with Duplicate State Elimination

Algo Delivery( CustomerList[], ProductOrderList[], ProductReceivedList[], AddressList[]):

    goalNotReached = TRUE
    explored :- map of explored states
    while goalNotReached
        State = [[customer1,order1, receive1, address1],...,[customer5,order5, receive5, address5]]
        if not explored(state)
            if IsGoal(state)
                print state
                goalNotReached = false
            else
                add to explored


Time Analysis:

For 4 runs

 No | Time to reach solution(minutes)
 1  | 1.200
 2  | 1.305
 3  | 7.127
 4  | 0.424

'''

import sys, os
import logging
import time
from copy import deepcopy
from math import ceil
import random

logging.basicConfig(level=logging.INFO) # log level

try:
    import queue
except ImportError:
    import Queue as queue


class Solution:
    def __init__(self):

        self.customers = ['F', 'G', 'H', 'I', 'J']
        self.orders = ['A', 'B', 'C', 'D', 'E']
        self.received = ['A', 'B', 'C', 'D', 'E']
        self.address = ['K', 'L', 'M', 'N', 'O']
        self.visited = {} # explored nodes
        self.start = time.time()
        self.end=0

    def printInitial(self):
        logging.info(self.initial)

    def getUID(self, data):
        uid = '';
        custF = '';
        custG = '';
        custH = '';
        custI = '';
        custJ = '';
        for node in data:
            if node[0] == 'F':
                custF = node
            elif node[0] == 'G':
                custG = node
            elif node[0] == 'H':
                custH = node
            elif node[0] == 'I':
                custI = node
            elif node[0] == 'J':
                custJ = node

        uid = ''.join(custF) + ''.join(custG) + ''.join(custH) + ''.join(custI) + ''.join(custJ)

        return uid

    def printMapping(self, data):

        names = {'F': 'Frank', 'G': 'George', 'H': 'Heather', 'I': 'Irene', 'J': 'Jerry', 'A': 'Amplifier',
                 'B': 'Banister', 'C': 'Candelabrum', 'D': 'Doorknob', 'E': 'Elephant', 'K': 'Kirkwood Street',
                 'L': 'Lake Avenue', 'M': 'Maxwell Street', 'N': 'North Avenue',
                 'O': 'Orange Drive'}

        self.end = time.time() - self.start
        logging.info("Execution time : " + str(round(self.end,2)) + ' seconds.')

        logging.info('\n ========================= Solution ====================================== ')
        for record in data:
            logging.info('Customer ' + names[record[0]] + ' ordered ' + names[record[1]] + ' but received ' + names[
                record[2]] + ' and lives at ' + names[record[3]])
        logging.info('\n ========================= End =========================================== ')

    def solve(self):
        repeatedNodes = 0
        while True:
            customers = deepcopy(self.customers)
            orders = deepcopy(self.orders)
            received = deepcopy(self.received)
            address = deepcopy(self.address)
            nodes = []
            for i in range(4, -1, -1):
                order = []
                order.append(customers.pop(random.randint(0, i)))
                order.append(orders.pop(random.randint(0, i)))
                order.append(received.pop(random.randint(0, i)))
                order.append(address.pop(random.randint(0, i)))
                nodes.append(order)
            logging.debug(nodes)

            # if already exists
            uid = self.getUID(nodes)
            if uid in self.visited:
                repeatedNodes += 1
                continue
            else:
                self.visited[uid] = '1'

            if self.isValid(nodes):
                logging.debug('Repeated nodes: ' + str(repeatedNodes))
                self.printMapping(nodes)
                break

    def isValid(self, data):

        customer = 0
        ordered = 1
        received = 2
        address = 3

        for orders in data:

            if ((orders[ordered] == orders[received]) or (orders[customer] == 'F' and orders[received] != 'D') or (
                            orders[ordered] == 'C' and orders[received] != 'B') or (
                            orders[received] == 'E' and orders[address] != 'N') or (
                            orders[received] == 'A' and orders[address] != 'M') or (
                            orders[customer] == 'G' and orders[address] == 'K') or (
                            orders[customer] == 'H' and orders[address] == 'O') or (
                            orders[ordered] == 'E' and orders[address] == 'M')):
                return False

        custBanister = '1'
        ipackage = '2'
        gOrder = '3'
        kReceive = '4'
        kOrder = '5'
        lReceive = '6'
        oOrder = '7'
        hReceive = '8'
        hOrder = '9'
        jReceive = '10'

        for orders in data:
            if orders[ordered] == 'B':
                custBanister = orders[received]
            if orders[customer] == 'I':
                ipackage = orders[ordered]
            if orders[customer] == 'G':
                gOrder = orders[ordered]
            if orders[address] == 'K':
                kReceive = orders[received]
                kOrder = orders[ordered]
            if orders[address] == 'L':
                lReceive = orders[received]
            if orders[address] == 'O':
                oOrder = orders[ordered]
            if orders[customer] == 'H':
                hReceive = orders[received]
                hOrder = orders[ordered]
            if orders[customer] == 'J':
                jReceive = orders[received]

        if custBanister != ipackage or gOrder != kReceive or kOrder != lReceive or oOrder != hReceive or hOrder != jReceive:
            return False

        return True


def main():
    solution = Solution()

    logging.info('Stared searching solution ..... ')

    solution.solve()

if __name__ == '__main__':
    main()
