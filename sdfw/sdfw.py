#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
提供APIの定義・実装
"""

__author__ = 'Nakaue Yoshito'
__date__ = '2022/03/23'

import sdfw
from sdfw.Messenger import Messenger
from sdfw.Mouse import Mouse
from sdfw.Point import Point
from sdfw.ValueHolder import ValueHolder as Value


def sdfw_init():
    """
    Initialize engine components.
    """
    Messenger.get_instance().start()


def sdfw_quit():
    """
    Quit process for engine components
    """
    Messenger.get_instance().exec_quit()


def update():
    """
    描画内容を更新する

    Returns
    -------
    is_loop : bool
        メインループが続くかどうか
    """
    Messenger.get_instance().exec_update()

    return True


def open_window(width, height):
    """
    新規ウィンドウを開く

    Parameters
    ----------
    width : int
        ウィンドウの横幅
    height : int
        ウィンドウの高さ

    Returns
    -------
    sdfw.window_index : int
        作成したウィンドウのID
    """
    Messenger.get_instance().exec_open_window(width, height)

    Value.get_instance().window_index += 1
    return Value.get_instance().window_index - 1


def close_window(win):
    """
    ウィンドウを閉じる

    Parameters
    ----------
    win : int
        削除するウィンドウID
    """
    Messenger.get_instance().exec_close_window(win)


def print_text(text, win=0):
    """
    指定文字列を指定ウィンドウに出力する

    Parameters
    ----------
    text : str
        出力する文字列
    win : int
        出力先ウィンドウID
    """
    Messenger.get_instance().exec_print_text(text, win)


def cursor_pos():
    """
    マウスカーソルの現在の座標を取得する

    Returns
    -------
    pos : Point
        現在のマウスカーソル座標
    """
    pos = Mouse.get_instance().get_current_position()
    return pos
