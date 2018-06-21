#一个阅读器的接口类
class Reader(object):
    def __init__(self):
        pass
    def load_setting(self):
        print('加载配置')

    def smart_broken_chapter(self):
        print('智能断章')

    def manually_broken_chapter(self):
        print('手动断章')

    def page_reading(self):
        print('章节阅读')

    def mark_add(self):
        print('添加书签')

    def research_all(self):
        print('全文搜索')

    def setting_themes(self):
        print('主题设置')
    
    def exit(self):
        print('退出保存')