#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
コマンドとイベント情報の送受信を行うクラスの実装
"""

__author__ = 'Nakaue Yoshito'
__date__ = '2022/03/23'

import socket
import threading
import time


class Messenger(threading.Thread):
    """
    コマンドとイベント情報の送受信を行う

    Attributes
    ----------
    ip_address : str
        IPアドレス（ローカルホスト）
    command_port : int
        コマンド送信用ポート番号
    event_port : int
        イベント情報受信用ポート番号
    buffer_size : int
        送受信バッファサイズ
    command_sock : socket
        コマンド送信用ソケット
    event_sock : socket
        イベント情報受信用ソケット
    """

    def __init__(self):
        """
        ソケット通信を開始する
        """
        super().__init__()
        print('Messenger is initialized')

        self.ip_address = '127.0.0.1'
        self.command_port = 62491
        self.event_port = 62492
        self.buffer_size = 512

        self.command_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.command_sock.connect((self.ip_address, self.command_port))

        self.event_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.event_sock.connect((self.ip_address, self.event_port))

    def run(self):
        """
        イベント情報受信スレッドでの実行処理
        """
        i = 0
        while True:
            print('Messenger is running.: ', end='')
            print(i)
            i += 1
            time.sleep(1)
