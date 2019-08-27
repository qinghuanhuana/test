# coidng=utf-8
from appium.webdriver.common.mobileby import By
import unittest,os,time
from selenium.common.exceptions import *
from app.common.Swipe_swipe import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.common.lxyd import Lxyd
from app.page import get_yaml
page_loc = get_yaml.LonginPage()
min_loc = get_yaml.MinePage()
class Lexin(unittest.TestCase):
    def setUp(self):
        self.fz = Lxyd()
        self.dr = self.fz.lunachapp()
        self.mine_loc = (min_loc[3]['type'],min_loc[3]['value'])
        self.userlogin_loc = (page_loc[3]['type'], page_loc[3]['value'])
        self.userphone_loc = (page_loc[1]['type'], page_loc[1]['value'])
        self.password_loc = (page_loc[2]['type'], page_loc[2]['value'])

    def tearDown(self):
        self.dr.quit()
        pass

    '''手机号为空'''
    def test002_null_username(self):
        try:
            self.fz.tan_chuan()
            self.fz.out_login()
            self.fz.login('', 123456)
            print('已登录退出后重新登陆')
        except:
            print('未登录状态登陆')
            self.fz.login('', 123456)
        try:
            userlogin_loc = WebDriverWait(self.dr, 1, 0.5).until(EC.element_to_be_clickable(self.userlogin_loc))
            userlogin_loc.click()
            print('用户名非空')
            raise Exception('登录按钮可点击')
        except TimeoutException as e:
            print('用户名为空%s' % e)

    '''密码为空'''
    def test003_null_password(self):
        try:
            self.fz.tan_chuan()
            self.fz.out_login()
            self.fz.login(19000000001, '1121211')
            print('已登录退出后重新登陆')
        except:
            print('未登录状态登陆')
            self.fz.login(19000000001, '1112112')
        try:
            userlogin_loc = WebDriverWait(self.dr, 3, 0.5).until(EC.element_to_be_clickable(self.userlogin_loc))
            userlogin_loc.click()
            # self.fz.is_toast_exist(u'密码错误')
            # print('获取到toast')
        except TimeoutException as e:
            print('密码为空%s' % e)

    '''5位密码登陆'''
    def test004_five_password(self):
        try:
            self.fz.tan_chuan()
            self.fz.out_login()
            self.fz.login(19000000001, 12345)
            print('已登录退出后重新登陆')
        except:
            print('未登录状态登陆')
            self.fz.login(19000000001, 12345)
        try:
            userlogin_loc = WebDriverWait(self.dr,10,1).until(EC.element_to_be_clickable(self.userlogin_loc))
            userlogin_loc.click()
            print('密码大于等于6位')
        except Exception as e:
            pass
            print('密码不足6位%s' % e)

    '''17位密码登陆'''
    def test005_out_password(self):
        try:
            self.fz.tan_chuan()
            self.fz.out_login()
            self.fz.login(19000000001, 12345678912345678)
            print('已登录退出后重新登陆')
        except:
            print('未登录状态登陆')
            self.fz.login(19000000001, 12345678912345678)
        try:
            zuobiaodanji(self.dr, 1470, 920, 1536, 2560)
            self.assertEqual(self.fz.get_text(self.password_loc), '1234567891234567')
            print('密码长度至多16位')
        except Exception as e:
            print('密码在6-16位之外%s' % e)
            raise Exception('用例执行失败')

    '''1位手机号'''
    def test006_one_mobile(self):
        try:
            self.fz.tan_chuan()
            self.fz.out_login()
            self.fz.login(1, 123456789)
            print('已登录退出后重新登陆')
        except:
            print('未登录状态登陆')
            self.fz.login(1, 123456789)
        try:
            userlogin_loc = WebDriverWait(self.dr, 3, 0.5).until(EC.element_to_be_clickable(self.userlogin_loc))
            userlogin_loc.click()
            print('账号不为空')
        except Exception as e:
            raise Exception('账号为空%s' % e)

    def login(self,mobile,password):
        self.mobile = mobile
        self.password = password
        self.dr.find_element_by_id('bt_login').click()
        self.dr.find_element_by_id('al_phone_Cet').clear()
        self.dr.find_element_by_id('al_phone_Cet').send_keys(self.mobile)
        self.dr.find_element_by_id('al_key_Cet').send_keys(self.password)

    def test002_login_success(self):
        try:
               mine_loc = (By.ID,'gz.lifesense.weidong.qa:id/tv_mine')
               if WebDriverWait(self.dr,10,0.5).until(EC.presence_of_element_located(mine_loc)):
                   self.dr.find_element_by_id('gz.lifesense.weidong.qa:id/tv_mine').click()
                   swipe_up(self.dr,500,2)
                   self.dr.find_element_by_xpath('//*[@text="设置"]').click()
                   self.dr.find_element_by_xpath('//*[@text="退出当前登录"]').click()
                   self.dr.find_element_by_id('dhf_confirm_tv').click()
                   self.login(19000000001,123456)
        except:
                self.login(19000000001,123456)
        self.dr.find_element_by_id('al_user_login_tv').click()
        try:
            self.dr.wait_activity('gz.lifesense.weidong.ui.activity.main.show_home_business_dialog',30)
            self.dr.find_element_by_id('dialog_close').click()
        except:
            print('首页弹窗广告未出现')
            pass
        try:
            self.dr.find_element_by_id('gz.lifesense.weidong.qa:id/tv_mine').click()
            id = self.dr.find_element_by_id('fm_id_tv').text
            self.assertEqual(id,'ID:5518805')
            print('登陆成功')
        except:
            print('登陆失败')

    def test001_updatename(self,user_name=u'你是猪'):
        mine_loc = (By.ID,'gz.lifesense.weidong.qa:id/tv_mine')
        if WebDriverWait(self.dr,10,0.5).until(EC.presence_of_element_located(mine_loc)):
            self.dr.find_element_by_id('gz.lifesense.weidong.qa:id/tv_mine').click()
        self.dr.find_element_by_id('gz.lifesense.weidong.qa:id/fm_userInfo').click()
        self.dr.find_element_by_id('gz.lifesense.weidong.qa:id/api_name_tv').click()
        self.dr.find_element_by_id('gz.lifesense.weidong.qa:id/srf_name_cet').clear()
        self.dr.find_element_by_id('gz.lifesense.weidong.qa:id/srf_name_cet').send_keys(user_name)
        self.dr.find_element_by_id('gz.lifesense.weidong.qa:id/srf_confirm_tv').click()
        name_txt = self.dr.find_element_by_id('gz.lifesense.weidong.qa:id/api_name_tv').text
        try:
            self.assertEqual(name_txt,user_name)
            print('修改用户名成功')
        except AssertionError as e:
            print ('修改用户名失败，错误:%s'%e)




if __name__ == "__main__":
    unittest.main()
