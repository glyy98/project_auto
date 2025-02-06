#搜索功能封装

from playwright.sync_api import Page


class SearchPage:
    def __init__(self,page:Page):
        self.page=page
        self.s_box="input[type='text']"
        self.s_button="input[type='button']"

