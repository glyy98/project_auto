#筛选框功能封装
from playwright.sync_api import Page

class FilterPage:
    def __init__(self,page:Page):
        self.page=page
        
    def apply_filter(self,filter_name:str,filter_value:str):
        self.page.get_by_text(filter_name).click() #点击筛选框
        self.page.get_by_text(filter_value).click()  #选择具体的选项


      
