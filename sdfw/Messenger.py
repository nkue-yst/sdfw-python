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
    _instance : Messenger
        シングルトン用インスタンス
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
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        """
        ソケット通信用のパラメータ設定を行い、通信を確立する
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
        スレッドにてイベント情報受信処理を行う
        """
        i = 0
        while i < 5:
            print('Messenger is running.: ', end='')
            print(i)
            i += 1
            time.sleep(1)

    def send_message(self, message):
        """
        作成したメッセージを送信する

        Parameters
        ----------
        message : str
            送信するメッセージ本体
        """
        # 同期用データを受信
        self.command_sock.recv(1)

        # 終端文字を付けたコマンド実行メッセージを送信
        self.command_sock.send((message + '\0').encode())

    def exec_quit(self):
        """
        終了処理を実行する
        """
        # 終了用メッセージを作成・送信
        message = 'quit'
        self.send_message(message)
