class StringHandler:
    def init(self): 
        pass 
    def getString(self):
        self.word = input() 
    def printString(self):
        print(self.word.upper())
        
s1 = StringHandler() 
s1.getString() 
s1.printString() 