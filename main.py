from selenium import webdriver
import time
import cv2
import random
from selenium.webdriver.support.wait import WebDriverWait
def track(dis):
    v=0
    t=0.2
    trace=[]
    p=0
    while  sum(trace)<dis:
        if  sum(trace)>(4/5)*dis:
            a=-0.2
        else:
            a=0.4
        v0=v
        p=round((1/2)*a*t**2+v*t+random.choice([2,3,1,0,2,1]),1)
        v=v0+a*t
        trace.append(p)
    if dis-sum(trace)<0:
        trace.pop()
    trace.append(abs(sum(trace)-dis))
    return trace
driver=webdriver.Chrome()
driver.get('http://passport.bilibili.com')
WebDriverWait(driver, 5, 0.5).until(lambda x: driver.find_element_by_xpath('//input[@id="login-username"]'))
driver.find_element_by_xpath('//input[@id="login-username"]').send_keys('18717123548')
WebDriverWait(driver, 5, 0.5).until(lambda x: driver.find_element_by_xpath('//input[@id="login-passwd"]'))
driver.find_element_by_xpath('//input[@id="login-passwd"]').send_keys('18717123548')
time.sleep(1)
WebDriverWait(driver, 5, 0.5).until(lambda x: driver.find_element_by_xpath('//div[@class="gt_slider_knob gt_show"]'))
e=driver.find_element_by_xpath('//div[@class="gt_slider_knob gt_show"]')
webdriver.ActionChains(driver).move_to_element(e).perform()
time.sleep(1)
driver.save_screenshot('a.png')
time.sleep(1)
e.click()
time.sleep(1)
webdriver.ActionChains(driver).move_to_element(e).perform()
time.sleep(1)
driver.save_screenshot('b.png')
import cv2
src=cv2.imread('a.png')
src_=cv2.imread('b.png')
bitwiseAnd=cv2.subtract(src,src_)#将图像image与M相减
ret, thresh = cv2.threshold(
    cv2.cvtColor(bitwiseAnd.copy(), cv2.COLOR_BGR2GRAY),  # 转换为灰度图像,
    20, 255,   # 大于127的改为255  否则改为0
    cv2.THRESH_BINARY)  # 黑白二值化
image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#查找轮廓
x,y,w,h=cv2.boundingRect(contours[-2])
x_,y_,w_,h_=cv2.boundingRect(contours[-1])
cv2.rectangle(src, (x, y), (x+w, y+h), (0, 25, 10), 2)
cv2.rectangle(src, (x_, y_), (x_+w_, y_+h_), (0, 25, 10), 2)
dis=abs(x-x_)-2
cv2.imshow("img", src)
cv2.waitKey(0)
webdriver.ActionChains(driver).click_and_hold(e).perform()
for i in track(dis):
    webdriver.ActionChains(driver).move_by_offset(i,0).perform()
    #time.sleep(random.choice([0.2,0.3,0.1,0.3,0.2,0.15]))
webdriver.ActionChains(driver).release().perform()
