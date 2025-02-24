import sys
import os

# 把项目根目录加入到 sys.path 中
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from playwright.sync_api import sync_playwright
from pages.filter_page import FilterPage


def test_data():
    with open("./data/test_data_filter.json", encoding="utf-8") as  f:
        data =json.load(f)
    return data['filters']

def test_page_filter():
    with sync_playwright() as p:
        # 启动浏览器并加载 session（免登录）
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="./config/session.json")  # 加载保存的 session   
        page = context.new_page()

        # 访问特定页面
        page.goto("http://192.168.100.214:19080/#/liveData/craneInfo/list")

        # 创建筛选功能对象
        filter_function = FilterPage(page)
 
        #获取测试数据
        filters=test_data()
        for filter_data in filters:
            filter_function.apply_filter(filter_data['filter_name'], filter_data['filter_value'])

        

        # 关闭浏览器
        browser.close()
        


