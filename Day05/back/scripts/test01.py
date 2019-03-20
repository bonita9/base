from appium import webdriver
import time


class TestAKLogin():

    def setup(self):
        # server 启动参数
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # app信息  /
        desired_caps['appPackage'] = 'com.vcooline.aike'
        desired_caps['appActivity'] = '.umanager.LoginActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # 错误用户名
    def test_erro_username(self):
        # 输入用户名
        self.driver.find_element_by_id("com.vcooline.aike:id/etxt_username").send_keys("1113222")
        # 输入密码
        self.driver.find_element_by_id("com.vcooline.aike:id/etxt_pwd").send_keys("1113222")
        # 点击登录
        self.driver.find_element_by_id("com.vcooline.aike:id/btn_login").click()

    # 用户名为空
    def test_usernmae_none(self):
        # 输入用户名
        self.driver.find_element_by_id("com.vcooline.aike:id/etxt_username").send_keys("")
        # 输入密码
        self.driver.find_element_by_id("com.vcooline.aike:id/etxt_pwd").send_keys("")
        # 点击登录
        self.driver.find_element_by_id("com.vcooline.aike:id/btn_login").click()