#-*- coding:utf-8 -*-
'''
处理视频播放
'''
from driverset.webDriverset import driver
import time
driver.get('http://videojs.com/')

print(driver.get_window_size())
driver.execute_script('window.scrollTo(0,1300)')

#需要iframe跳转
driver.switch_to_frame(2)

time.sleep(10)
video=driver.find_element_by_id('vjs_video_3_html5_api')
'//*[@id="preview-player_html5_api"]'
#返回视频播放地址
url=driver.execute_script('return arguments[0].currentSrc;',video)
print(url)
time.sleep(5)

#播放视频
print('start the video')
driver.execute_script('return arguments[0].play()',video)

#播放5S
time.sleep(20)
#暂停
driver.execute_script('return arguments[0].pause()',video)

print('video has paused')