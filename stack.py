class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__top==self.__max_size-1:
            return True
        else:
            return False
        #Remove pass and write the logic to check whether stack is full. If the stack is full, return true else return false.

    def push(self,data):
        if self.is_full()==False:
            self.__top+=1
            self.__elements[self.__top]=data
        else:
            print("stack full")
            
        #Remove pass and write the logic to push element into the stack. Element should be pushed only if the stack is not full. Otherwise, display appropriate message
         
    def is_empty(self):
        if self.__top==-1:
            return True
        else:
            return False
        #Remove pass and write the logic to check whether stack is empty. If the stack is empty, return true else return false.
    
    def pop(self):
        if self.is_empty()==False:
            self.__top-=1
        #Remove pass and write the logic to pop an element. Pop the element only if stack is not empty. Otherwise, display appropriate message
        
    def display(self):
        index=self.__top
        while(index>=0):
            print(self.__elements[index])
            index-=1
        #Remove pass and write the logic to display the element(s).    
                                              
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

stack1=Stack(5)
#Push all the required element(s).
stack1.push("Shirt1")
stack1.push("shirt2")
stack1.push("shirt3")
#stack1.pop()
stack1.pop()
#print(stack1)
stack1.display()
