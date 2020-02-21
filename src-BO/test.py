# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 23:00
# @Author  : Leon
# @Email   : 1446684220@qq.com
# @File    : test.py
# @Desc    :
# @Software: PyCharm

from WechatPCAPI import WechatPCAPI
import time
import logging
from queue import Queue
import threading


logging.basicConfig(level=logging.INFO)
queue_recved_message = Queue()


# 这是消息回调函数，所有的返回消息都在这里接收，建议异步处理，防止阻塞
def on_message(message):
    print(message)


def main():
    wx_inst = WechatPCAPI(on_message=on_message, log=logging)
    wx_inst.start_wechat(block=True)

    while not wx_inst.get_myself():
        time.sleep(5)

    print('登陆成功')
    print(wx_inst.get_myself())

    time.sleep(10)
    # wx_inst.send_text(to_user='filehelper', msg='作者QQ:\r1446684220')
    wx_inst.send_img(to_user='filehelper', img_abspath=r'C:\Users\Leon\Pictures\1.jpg')
    time.sleep(1)
    wx_inst.send_link_card(
        to_user='filehelper',
        title='博客',
        desc='我的博客，红领巾技术分享网站',
        target_url='http://www.honglingjin.online/',
        img_url='http://honglingjin.online/wp-content/uploads/2019/07/0-1562117907.jpeg'
    )
    time.sleep(1)

    # 这个是获取群具体成员信息的，成员结果信息也从上面的回调返回
    # wx_inst.get_member_of_chatroom('22941059407@chatroom')

    # 这个是更新所有好友、群、公众号信息的，结果信息也从上面的回调返回
    # wx_inst.get_friends()


if __name__ == '__main__':
    main()
