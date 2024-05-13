class Stack:
    def __init__(self):
        self.stk = []
    def is_empty(self) :
        return len(self.stk) == 0
    def push(self,item):
        return self.stk.append(item)
    def pop(self) :
        if len(self.stk) == 0 :
            print("The stack is empty")
            return 0
        else :
            return self.stk.pop()
    def peek(self) :
        if len(stk) == 0 :
            print("The stack is empty")
            return 0
        else :
            return self.stk[-1]
    def size(self) :
        return len(self.stk)
    def display(self):
        print(self.stk)
    

if __name__ == '__main__' :
    s = Stack()
    s.push(4)
    s.push(3)
    s.pop()
    s.display()
    
    
    

    
    
        
        