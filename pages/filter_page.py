#筛选框功能封装
from playwright.sync_api import Page

class FilterPage:
    def __init__(self,page:Page):
        self.page=page
        
    def apply_filter(self,filter_name:str,filter_value:str):
        self.page.get_by_text(filter_name).click() #点击筛选框
        #选择具体的选项,li:has-text(""),查找列表中，值为filter_value的
        self.page.locator(f'li:has-text("{filter_value}")').click()
        
    
