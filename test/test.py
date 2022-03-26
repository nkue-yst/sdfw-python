#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SDFWを利用したテストプログラム
"""

__author__ = 'Nakaue Yoshito'
__date__ = '2022/03/24'

import sdfw
import time


def main():
    """
    sdfwを利用したテストプログラムのメイン処理関数
    """
    sdfw.sdfw_init()
    sdfw.open_window(1280, 720)

    while sdfw.update():
        time.sleep(1)

    sdfw.sdfw_quit()


if __name__ == '__main__':
    main()
