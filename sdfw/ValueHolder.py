#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
各種変数を保管するクラスの実装
"""

__author__ = 'Nakaue Yoshito'
__date__ = '2022/03/28'


class ValueHolder:
    """
    各機能から参照する変数を保管するクラス

    Attributes
    ----------
    _instance : ValueHolder
        シングルトン用インスタンス
    window_index : int
        最後に作成したウィンドウのID
    """
    _instance = None

    @classmethod
    def get_instance(cls):
        """
        シングルトンのインスタンスを取得する

        Returns
        -------
        _instance : ValueHolder
            シングルトン用インスタンス
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.window_index = 0
