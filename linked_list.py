class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        node=Node(data)
        if self.__tail==None:
            self.__head=node
            self.__tail=node
        else:
            self.__tail.set_next(node)
            self.__tail=node   
        #Remove pass and copy the code you had written to add an element.
    
    def display(self):
        temp=self.__head
        while(temp!=None):
            print(temp.get_data())
            temp=temp.get_next()
        #Remove pass and copy the code you had written to display the element(s).
    
    def find_node(self,data):
        if self.__tail==None:
            return None
        temp=self.__head
        flag=0
        while(temp!=None):
            if temp.get_data()==data:
                flag=1
                return temp
            temp=temp.get_next()
        if flag==0:
            return None    
        #Remove pass and copy the code you had written to find the node containing the element.
    
    def insert(self,data,data_before):
        node=Node(data)
        node_before=self.find_node(data_before)
        if node_before!=None:
            node.set_next(node_before.get_next())
            node_before.set_next(node)
        else:
            print("Node not found")    
        #Remove pass and write the logic to insert an element.
        
    def delete(self,data):
        temp=self.__head
        if temp.get_data()==data:
            self.__head=temp.get_next()
            if self.__tail.get_data()==data:
                self.__tail=None
        else:
            while(temp!=None):
                if temp.get_next().get_data()==data:
                    temp.set_next(temp.get_next().get_next())
                    if self.__tail==data:
                        self.__tail=temp
                    break
                temp=temp.get_next()                         
             
        #Remove pass and write the logic to delete an element.    
                                              
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


list1=LinkedList()
list1.add("Sugar")
list1.add(None)
list1.add("Salt")
list1.add(None)
#Add all the required element(s)
#Insert the element in the required position
list1.insert("NewItem","Salt")
#list1.delete("Sugar")
list1.display()
                                              