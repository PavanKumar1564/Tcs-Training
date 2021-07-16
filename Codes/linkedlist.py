class nnode:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class llist:
    def __init__(self):
        self.head=None
    
    
    def insertab(self,data):
        node=nnode(data)
        node.next=self.head
        self.head=node
    
    
    def insertae(self,data):
        node=nnode(data)
        
        k=self.head
        
        if self.head is None:
            self.head=node
        else:
            while k.next:
                k=k.next
        
            k.next=node
        
    
    def printl(self):
        a=self.head
        if not a:
            print("empty")
        else:
            while a:
                print(a.data)
                a=a.next
                
    
    def length(self):
        itr=self.head
        c=0
        while itr:
            c=c+1
            itr=itr.next
        print(c)
        return c

            
    def reverse(self):
        prev=None
        curr=self.head
        while curr!=None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev
            
    
    def addatpos(self,data,p):
        node=nnode(data)
        itr=self.head
        for i in range(p-2):
            itr=itr.next
        
        node.next=itr.next
        itr.next=node

        
    def delatb(self):
        self.head=self.head.next
        
    def delate(self):
        itr=self.head
        while itr.next.next:
            itr=itr.next
            
        itr.next=None
        
    def delatp(self,p):
        itr=self.head
        for i in range(p-2):
            itr=itr.next
            
        itr.next=itr.next.next