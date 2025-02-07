from playwright.sync_api import sync_playwright

# 配置登录信息
LOGIN_URL = "http://192.168.100.214:19080/#/login"  # 替换为你的登录页面URL
USERNAME = "superadmin"
PASSWORD = "123456"
SESSION_FILE = "./config/session.json"  # 存储会话的文件路径


def login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 关闭 headless 以观察执行情况
        context = browser.new_context()  # 创建新的浏览器上下文
        page = context.new_page()
        
        # 访问登录页面
        page.goto(LOGIN_URL)
        
        # 填写用户名和密码

        #注意，fill方法需要的是css选择器，没有加//input时候就是xpath写法，
        page.fill("//div[@class='input-group user']//input", USERNAME)
        page.fill("//div[@class='input-group pwd']//input", PASSWORD)
        
        # 点击登录按钮
        page.click("button[type='button']")
        
        # 等待 URL 中包含 'dashboard' 字样
        page.wait_for_url("**/dashboard/index")  

        # 保存会话状态（cookies 和 localStorage）
        context.storage_state(path=SESSION_FILE)

        
        print("登录成功！")
        
        # 关闭浏览器
        browser.close()

if __name__ == "__main__":
    login()
