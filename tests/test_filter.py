import json
from playwright.sync_api import sync_playwright
from pages.filter_page import FilterPage

def test_data():
    with open("./data/test_data_filter.json") as f:
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

        # 应用筛选功能
        filter_function.apply_filter("category", "Electronics")

        # 确认筛选结果
        page.wait_for_selector("div.filtered-results")

        print("筛选功能测试通过！")

        # 关闭浏览器
        browser.close()
