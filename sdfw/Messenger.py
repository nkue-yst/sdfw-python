#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
コマンドとイベント情報の送受信を行うクラスの実装
"""

__author__ = 'Nakaue Yoshito'
__date__ = '2022/03/23'

import socket
import threading
from sdfw.Mouse import Mouse


class Messenger(threading.Thread):
    """
    コマンドとイベント情報の送受信を行う

    Attributes
    ----------
    _instance : Messenger
        シングルトン用インスタンス
    _is_loop : bool
        メインループが続くかどうか
    _ip_address : str
        IPアドレス（ローカルホスト）
    _command_port : int
        コマンド送信用ポート番号
    _event_port : int
        イベント情報受信用ポート番号
    _buffer_size : int
        送受信バッファサイズ
    _command_sock : socket
        コマンド送信用ソケット
    _event_sock : socket
        イベント情報受信用ソケット
    """
    _instance = None

    @classmethod
    def get_instance(cls):
        """
        シングルトンのインスタンスを取得する

        Returns
        -------
        _instance : Messenger
            シングルトン用インスタンス
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        """
        ソケット通信用のパラメータ設定を行い、通信を確立する
        """
        super().__init__()

        self._is_loop = True

        self._ip_address = '127.0.0.1'
        self._command_port = 62491
        self._event_port = 62492
        self._buffer_size = 512

        self._command_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._command_sock.connect((self._ip_address, self._command_port))

        self._event_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._event_sock.connect((self._ip_address, self._event_port))

    def run(self):
        """
        スレッドにてイベント情報受信処理を行う
        """
        sync_message = '0'
        str_buff = ''
        self._event_sock.send(sync_message.encode())

        while self._is_loop:
            buff = self._event_sock.recv(1).decode()

            if buff == '\0':
                word_list = self._parse_message(str_buff)

                if word_list[0] == 'Mouse':
                    if word_list[1] == 'Button':
                        if word_list[2] == 'Down':
                            Mouse.get_instance().on_button_down(word_list[3], word_list[4], word_list[5])
                        elif word_list[2] == 'Up':
                            Mouse.get_instance().on_button_up(word_list[3], word_list[4], word_list[5])
                    elif word_list[1] == 'X':
                        Mouse.get_instance().update_position(word_list[2], word_list[4])

                str_buff = ''
                word_list = []
                self._event_sock.send(sync_message.encode())
            else:
                str_buff += buff

    @staticmethod
    def _parse_message(message, delimiter='/'):
        """
        メッセージを区切り文字で区切って返す

        Parameters
        ----------
        message : str
            元のメッセージ
        delimiter : str
            区切り文字

        Returns
        -------
        word_list : list
            区切った文字列リスト
        """
        word_list = message.split(delimiter)
        return word_list

    def _send_message(self, message):
        """
        作成したメッセージを送信する

        Parameters
        ----------
        message : str
            送信するメッセージ本体
        """
        # 同期用データを受信
        self._command_sock.recv(1)

        # 終端文字を付けたコマンド実行メッセージを送信
        self._command_sock.send((message + '\0').encode())

    def exec_quit(self):
        """
        終了処理を実行する
        """
        # 終了用メッセージを作成・送信
        message = 'quit'
        self._send_message(message)
        self._is_loop = False

    def exec_update(self):
        """
        描画内容の更新処理を実行する
        """
        # フレーム更新用メッセージを作成・送信
        message = 'update'
        self._send_message(message)

    def exec_open_window(self, width, height):
        """
        新規ウィンドウを開く

        Parameters
        ----------
        width : int
            ウィンドウの横幅
        height : int
            ウィンドウの高さ
        """
        # ウィンドウ作成用メッセージを作成・送信
        message = 'openWindow/' + str(width) + '/' + str(height)
        self._send_message(message)

    def exec_close_window(self, win):
        """
        ウィンドウを閉じる

        Parameters
        ----------
        win : int
            削除するウィンドウID
        """
        # ウィンドウ削除用メッセージを作成・送信
        message = 'closeWindow/' + str(win)
        self._send_message(message)

    def exec_print_text(self, text, win):
        """
        指定文字列を指定ウィンドウに出力する

        Parameters
        ----------
        text : str
            出力する文字列
        win : int
            出力先ウィンドウID
        """
        # 文字列出力用メッセージを作成・送信
        message = 'print/' + text + '/' + str(win)
        self._send_message(message)
