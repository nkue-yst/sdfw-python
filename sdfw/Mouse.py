#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
マウスの状態を管理するクラスの実装
"""

__author__ = 'Nakaue Yoshito'
__date__ = '2022/03/27'

from sdfw.Point import Point


class MouseButton:
    """
    マウスボタン押下状態の管理クラス

    Attributes
    ----------
    is_pressed : bool
        押されているかどうか
    """

    def __init__(self):
        """
        押されていない状態で初期化
        """
        self.is_pressed = False


class Mouse:
    """
    マウスの状態を管理するクラス

    Attributes
    ----------
    _instance : Mouse
        シングルトン用インスタンス
    _current_pos : Point
        現在のマウスカーソル座標
    _left_button : MouseButton
        マウス左ボタン
    _middle_button : MouseButton
        マウス中央ボタン
    _right_button : MouseButton
        マウス右ボタン
    """
    _instance = None

    @classmethod
    def get_instance(cls):
        """
        シングルトンのインスタンスを取得する

        Returns
        -------
        _instance : Mouse
            シングルトン用インスタンス
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        """
        マウス状態管理クラスの初期化
        """
        super(Mouse, self).__init__()

        self._current_pos = Point()
        self._left_button = MouseButton()
        self._middle_button = MouseButton()
        self._right_button = MouseButton()

    def get_current_position(self):
        """
        現在のカーソルの座標を取得する

        Returns
        -------
        pos : Point
            現在のカーソル座標
        """
        pos = self._current_pos
        return pos

    def on_button_down(self, button_name, x, y):
        """
        マウスボタンの押下時処理

        Parameters
        ----------
        button_name : str
            押下されたマウスボタンの名前
        x : int
            押下されたx座標
        y : int
            押下されたy座標
        """
        if button_name == 'LEFT':
            self._left_button.is_pressed = True
        elif button_name == 'MIDDLE':
            self._middle_button.is_pressed = True
        elif button_name == 'RIGHT':
            self._right_button.is_pressed = True

        self._current_pos = Point(x, y)

    def on_button_up(self, button_name, x, y):
        """
        マウスボタンの離した時の処理

        Parameters
        ----------
        button_name : str
            離されたマウスボタンの名前
        x : int
            離されたx座標
        y : int
            離されたy座標
        """
        if button_name == 'LEFT':
            self._left_button.is_pressed = False
        elif button_name == 'MIDDLE':
            self._middle_button.is_pressed = False
        elif button_name == 'RIGHT':
            self._right_button.is_pressed = False

        self._current_pos = Point(x, y)

    def update_position(self, x, y):
        """
        カーソルの座標を更新する

        Parameters
        ----------
        x : int
            現在のx座標
        y : int
            現在のy座標
        """
        self._current_pos = Point(x, y)
