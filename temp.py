#!/usr/bin/python3
# coding:utf-8 
import requests
import sys
import os
from datetime import datetime

# 設定値
path = "/sys/bus/w1/devices/"

# センサーディレクトリ確認
files = os.listdir(path)
files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]

for files in files_dir:

    # 「28-」で始まるもの
    if not files.find('28-') == -1:

        # ディレクトリ
        sensor_w1_slave = "/sys/bus/w1/devices/" + files + "/w1_slave"

        # 文字列読み取り
        with open(sensor_w1_slave) as f:
            list = f.readlines()

        # 2行目
        temp_val = list[1].split("=")

        # 温度を取得
        temp_val = int(temp_val[1]) / 1000

sys.exit()