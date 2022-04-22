from numpy.random import randint
import numpy as np


# Classes to simulate the Tangle

class Transaction:

    def __init__(self, ID):
        self.ID = ID
        self.children = []
        self.age = 0

    def attach(self, children):

        for child in set(children):
            self.children.append(child)

    def setAge(self, t):

        self.age += t



class Tangle:

    def __init__(self, PoW):

        self.nOfTransactions = 1
        self.h = PoW
        genesis = Transaction(0)
        self.transactions = [genesis]
        self.transactionsPending = []
        self.tips = [genesis]
        



    def newTransaction(self, k, q = 1):

        
        tx = Transaction(self.nOfTransactions + 1)
        
        if np.random.random() > q:

                tx.attach(self.randomSelection(0))

        else:

                tx.attach(self.randomSelection(k))
        
        self.addTransaction(tx)






    def addTransaction(self, transaction):

        self.transactionsPending.append(transaction)
        self.transactions.append(transaction)
        self.nOfTransactions += 1






    def checkPoW(self):


        for tx in self.transactionsPending:
            
            if tx.age >= self.h:

                self.transactionsPending.remove(tx)
                self.tips.append(tx)

                for child in tx.children:
                    
                    
                    if child in self.tips:
                        self.tips.remove(child)

                        
        return len(self.tips)
    



    def increaseAge(self, t):

        for transaction in self.transactions:

            transaction.setAge(t)



    
    def randomSelection(self, k):
        
        length = len(self.tips)
        selections = [self.tips[randint(length)] for i in range(k)]

        return selections
