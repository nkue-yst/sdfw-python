#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
座標を示すためのクラス
"""

__author__ = 'Nakaue Yoshito'
__date__ = '2022/03/27'


class Point:
    """
    座標を示すポイントクラス

    Attributes
    ----------
    x : int
        x座標
    y : int
        y座標
    """

    def __init__(self, x=0, y=0):
        """
        変数を初期化する

        Parameters
        ----------
        x : int
            x座標
        y : int
            y座標
        """
        self.x = x
        self.y = y
