#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
提供APIの定義・実装
"""

__author__ = 'Nakaue Yoshito'
__date__ = '2022/03/23'

from sdfw.Messenger import Messenger


def sdfw_init():
    """
    Initialize engine components.
    """
    messenger = Messenger.get_instance()
    messenger.start()
    messenger.join()


def sdfw_quit():
    """
    Quit process for engine components
    """
    messenger = Messenger.get_instance()
    messenger.exec_quit()
