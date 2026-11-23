class ProductOfNumbers(object):

    def __init__(self):
        self.pref =[1]        

    def add(self, num):
        if num == 0:
            self.pref = [1] 
        else:
            self.pref.append(self.pref[-1] * num)               

    def getProduct(self, k):
        if k >= len(self.pref):
            return 0
        return self. pref[-1] // self.pref[-k - 1]

        


        
        


