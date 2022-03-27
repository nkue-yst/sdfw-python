#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SDFWを利用したテストプログラム
"""

__author__ = 'Nakaue Yoshito'
__date__ = '2022/03/24'

import sdfw


def main():
    """
    sdfwを利用したテストプログラムのメイン処理関数
    """
    sdfw.sdfw_init()
    sdfw.open_window(1280, 720)

    while sdfw.update():
        sdfw.print_text(str(sdfw.cursor_pos().x) + ', ' + str(sdfw.cursor_pos().y))

    sdfw.sdfw_quit()


if __name__ == '__main__':
    main()
