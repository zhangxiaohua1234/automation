from selenium import webdriver #导包
from selenium.webdriver.support.ui import Select #导包 里面封装了方法
# dr=webdriver.Firefox()
# dr.get("file:///D:/%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E9%A2%98/%E4%B8%8B%E8%BD%BD/control.html")


                               # “selenium之selecet元素定位，及多个相同元素如何定位”
# Select只对<select>标签的下拉菜单有效、才可以使用）
# Select(dr.find_element_by_class_name("u17")).select_by_value("3") #根据class定位，使用value进行选择
# Select(dr.find_element_by_id("areaID")).select_by_visible_text("北京") #根据ID定位，使用文字进行选择
# Select(dr.find_element_by_id("areaID")).select_by_index(1) #根据ID定位，使用index进行索引数字
# 在html中 u 有多个值，使用elements，在多个里边选择某一个
# dr.find_elements_by_id("u")
# print(type(dr.find_elements_by_id("u")))  #选择前，打印这条数据类型，结果是列表类型
# 多选春夏秋冬
# dr.find_elements_by_id("u")[0].click() #在列表类型中有多个值时，可以使用[]定位某一个值
# dr.find_elements_by_id("u")[1].click()
# dr.find_elements_by_id("u")[2].click()
# dr.find_elements_by_id("u")[3].click()

                                          # 9.24 selenium之多个的元素定位，切换alert
# html页面进行多选操作方法，使用for循环替换上面的多选
# for i in dr.find_elements_by_id("u"):
#     i.click()

# s=dr.find_elements_by_id("u")
# for n in s:
#     if s.index(n)%2==0:
#         n.click()




                                                # 第一百九十九节 xpath和alert
# 练习网页
import time  #导入time
# dr=webdriver.Firefox()
# dr.get("http://sahitest.com/demo/index.htm")
# dr.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/a[1]").click()  #xpath 进入网址 Link Test
# dr.find_element_by_css_selector("a.a:nth-child(1)").click()  #css选择器进入网址 Link Test
# dr.find_element_by_css_selector("html body table tbody tr td a.a.x")#css路径进入网址 Link Test
# dr.find_element_by_xpath("/html/body/table/tbody/tr/td[3]/a[1]").click()  #使用xpath进入网址 Alert Test
# time.sleep(2)
# dr.find_element_by_name("b1").click()
# time.sleep(2)
# aler=dr.switch_to.alert#切换到弹窗；赋值给变量aler
# aler.accept()#点击确定
# time.sleep(2)
# dr.back()#返回
# time.sleep(2)
# dr.find_element_by_xpath("/html/body/table/tbody/tr/td[3]/a[2]").click()
# time.sleep(2)
# # dr.find_element_by_xpath("/html/body/form/input[1]").click()
# dr.find_element_by_name("b1").click()
# time.sleep(2)
# aler.dismiss()#取消
# dr.back()#返回
#
# dr.find_element_by_xpath("/html/body/table/tbody/tr/td[3]/a[3]").click()
# time.sleep(2)
# # dr.find_element_by_xpath("/html/body/form/input[1]").click()
# dr.find_element_by_name("b1").click()
# time.sleep(2)
# aler.send_keys("445126")
# time.sleep(2)
# aler.accept()#确定



                                                                     #作业 进入禅道
# dr=webdriver.Firefox()
# dr.get("http://115.28.108.130/zentaopms/www/index.php?m=user&f=login")
# dr.find_element_by_id("account").send_keys("zhangdebao")
# dr.find_element_by_name("password").send_keys("123456")
# # time.sleep(2)
# dr.find_element_by_id("submit").click()#点击登录
# # time.sleep(2)
# dr.find_element_by_id("menuqa").click()
# # time.sleep(2)
# dr.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[1]/div[2]/a[2]").click()
# # time.sleep(2)
# dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/form/table/tbody/tr[1]/td[1]/div/a/span").click()
# dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/form/table/tbody/tr[1]/td[1]/div/div/ul/li[37]").click()
# # time.sleep(2)
# dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/form/table/tbody/tr[1]/td[2]/div/div/a").click()
# dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/form/table/tbody/tr[1]/td[2]/div/div/div/ul/li[3]").click()#选择个人中心
# dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/form/table/tbody/tr[2]/td/span/div/a").click()
# dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/form/table/tbody/tr[2]/td/span/div/div/ul/li[1]").click() #选择在线教育23期
# # dr.find_element_by_class_name("active-result").select_by_index("1") 错误
# dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/form/table/tbody/tr[3]/td[1]/span/div/ul").click()
# dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/form/table/tbody/tr[3]/td[1]/span/div/div/ul/li").click() #选择trunk
# dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/form/table/tbody/tr[4]/td/span/div/a").click()
# dr.find_element_by_xpath("/html/body/div[1]/div[1]/div/form/table/tbody/tr[4]/td/span/div/div/ul/li[1]").click() #选择管理员
# dr.find_element_by_id("title").send_keys("啊书法大赛")
# # dr.find_element_by_xpath("/html/body/p[1]").click()错误
# dr.find_element_by_id("submit").submit()
#

