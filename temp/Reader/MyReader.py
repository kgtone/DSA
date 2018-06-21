import json
import re
# from collections import OrderedDict
from Reader import Reader
class book_info(object):
    def __init__(self):
        #书籍存储的位置
        self.bpath=None
        #章节名匹配正则表达式字符串
        self.reg=None
        #章节名存储的chapters{章节名：文件指针（int)}
        self.chapters=TwoElemDict()
        #书签
        self.mark=TwoElemDict()
        #最后一次打开的那个点，类型是int
        self.last=None

class TwoElemDict(object):
    def __init__(self):
        self.dic={}
        self.length=0

    def getLength(self):
        return self.length
    
    def clearDict(self):
        self.dic.clear()
        self.length=0

    def key2Str(self,key):
        key=str(key)
        if len(key)>5 or len(key)<1:
            print('序号长度不对')
        if len(key)==5:
            return    
        elif len(key)==1:
            key='0000'+key
        elif len(key)==2:
            key='000'+key
        elif len(key)==3:
            key='00'+key
        elif len(key)==4:
            key='0'+key
        return key
        
    def add(self,value1,value2):
        # print('chapter')
        key=self.key2Str(self.length+1)        
        if key in self.dic:
            print('放入的序号已经存在')
            return
        v=[value1,value2]
        self.dic[key]=v
        self.length=int(key)


    def viewInfo(self):
        for i in range(1,self.length+1):
            i=self.key2Str(i)
            print(str(i),' ',self.dic[i][0])
    
    def getChapterPoint(self,key):
        key=self.key2Str(key)
        if key in self.dic:
            return self.dic[key][1]

class MyReader(object):
    def __init__(self,settings):
        self.bookinfo=book_info()
        self.settings=settings
        #######
        self.fbook=None
        

        def load_setting():
            #加载配置文件
            if not self.settings=='':
                try:
                    t=open(self.settings,'r',encoding='utf-8')
                    d=json.load(t)
                    self.bookinfo.bpath=d['bpath']
                    self.bookinfo.reg=d['reg']
                    #here
                    # self.bookinfo.chapters=d['chapters']
                    self.bookinfo.mark=d['mark']
                    self.bookinfo.last=d['last']
                except IOError as e:
                    print('配置文件出错，请检查配置文件')
                finally:
                    t.close()
                #加载
                if not self.bookinfo.bpath=='':
                    try:
                        self.fbook=open(self.bookinfo.bpath,'r',encoding='utf-8')
                    except IOError as identifier:
                        print('该目录下面找不到book')
                    finally:
                        # self.fbook.close()        
                        pass
        load_setting()

            
    # def broken_chapter(self):
    #     if not self.bookinfo.reg==None:
    #         self.bookinfo.chapters.clear()
    #         pattern=re.compile(self.bookinfo.reg)
    #         ch=self.fbook.tell()
    #         line=self.fbook.readline()            
    #         while line:
    #             if not pattern.search(line)==None:
    #                 start,end=pattern.search(line).span()
    #                 key=line[start:end]
    #                 value=ch
    #                 self.bookinfo.chapters[key]=value
    #             ch=self.fbook.tell()
    #             line=self.fbook.readline()

            

    def broken_chapter(self):
        self.bookinfo.chapters.clearDict()
        pattern=re.compile(self.bookinfo.reg)
        p=self.fbook.tell()
        line=self.fbook.readline()
        while line:
            if not pattern.search(line)==None:
                start,end=pattern.search(line).span()
                value1=line[start:end]
                value2=p
                self.bookinfo.chapters.add(value1,value2)
            p=self.fbook.tell()
            line=self.fbook.readline()
        self.bookinfo.chapters.viewInfo()
            

            
            

    def page_reading(self):
        pass
 
    def mark_add(self):
        pass

    def research_all(self):
        pass

    def setting_themes(self):
        pass

    def exit(self):
        pass


r=MyReader('./book.json')
r.broken_chapter()