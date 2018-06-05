class Node(object):
    def __init__(self,val,p=None):
        self.data=val
        self.next=p

class linklist(object):
    def __init__(self):
        self.length=0
        self.next=None

    # # def InitList(self):
    # #     pass
    
    #OK
    def DestroyList(self):
        self.next=None
    
    #OK
    def ClearList(self):
        self.length=0
        self.next=None

    #OK
    def ListEmpty(self):
        if self.length==0:
            return True
        else:
            return False
    
    #OK
    def ListLength(self):
        return self.length

    #OK
    def GetElem(self,i):
        p=self
        j=-1
        while(j<i):
            if p.next!=None:
                p=p.next
                j+=1
        e=p.data
        return e
    
    #OK
    def LocateElem(self,e):
        p=self
        j=-1
        while p.next!=None:
            p=p.next
            j+=1
            if p.data==e:
                return j
        return False
    
    #OK
    def PriorElem(self,cur_e):
        p=self
        j=-1
        while p.next!=None:
            p=p.next
            j+=1
            if j==0 and p.data==cur_e:
                print('there is the first elem of linklist')
                return None                
            if j<self.length-1 and p.next.data==cur_e:
                pre_e=p.data
                return pre_e
        print('None')        
        return None

    def NextElem(self,cur_e):
        p=self
        while p.next!=None:
            p=p.next
            if p.data==cur_e:
                if p.next==None:
                    print('None')
                    return None
                else:
                    return p.next.data
        print('None')
        return None

    # def ListInsert(self,i,e):
        

    # #此处i为索引，从0开始
    # def ListDelete(self,i):
    #     j=-1
    #     p=self
    #     while j<i:
    #         p_pre=p.next
    #         j+=1
    #     p_next=p_pre.next.next

        
        
    #     return del_e

    #OK
    def ListTraverse(self):
        #拿到链表头部，开始往下遍历，直到尾部
        p=self
        if p.next==None:
            print('the linklist is empty!')
        while p.next!=None:
            p=p.next
            print(p.data)
    
    #OK
    def Add(self,e):
        #拿到链表头部，寻找链表尾部
        p=self
        while p.next!=None:
            p=p.next
        #构造链表节点Node,data的值为e，next指向None
        t=Node(e,None)
        #把尾巴挂上去
        p.next=t
        #增加链表的长度
        self.length+=1
            
            





    

