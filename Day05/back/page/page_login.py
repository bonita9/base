class PageLogin:
    def __init__(self, driver):
        self.driver = driver

    # 输入用户名
    def page_input_username(self, username):
        self.driver.find_element_by_id("com.vcooline.aike:id/etxt_username").send_keys(username)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.driver.find_element_by_id("com.vcooline.aike:id/etxt_pwd").send_keys(pwd)


    # 点击登录
    def page_click_login_btn(self):
        self.driver.find_element_by_id("com.vcooline.aike:id/btn_login").click()

    # 组装登录方法
    def page_login(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
