#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用os模块编写一个能实现dir -l输出的程序。
# 列出当前目录的详细列表（权限、大小、时间等）。

from datetime import datetime
import os

pwd = os.path.abspath(".")

print("      Size     Last Modified  Name")
print("------------------------------------------------------------")

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    # 将时间戳转换成datetime对象，才能使用strftime
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime("%Y-%m-%d %H:%M") 
    flag = "/" if os.path.isdir(f) else ""
    print("%10d  %s  %s%s" % (fsize, mtime, f, flag))


# 利用os模块编写一个能实现dir -l输出的程序。

import time

# 定义一个函数list_directory，用来列出指定目录下的所有文件和文件夹
def list_directory(path):
    # 使用os.scandir()函数扫描指定目录下的所有文件和文件夹
    entries = os.scandir(path)
    # 遍历每一个文件和文件夹
    for entry in entries:
        # 获取文件和文件夹的权限
        permissions = entry.stat().st_mode & 0o777
        # 获取文件和文件夹的硬链接数
        hard_links = entry.stat().st_nlink
        # 获取文件和文件夹的所有者
        owner = entry.stat().st_uid
        # 获取文件和文件夹的所有组
        group = entry.stat().st_gid
        # 获取文件和文件夹的大小
        size = entry.stat().st_size
        # 获取文件和文件夹的最后修改时间
        mtime = time.ctime(entry.stat().st_mtime)
        # 获取文件和文件夹的名称
        filename = entry.name
        # 打印文件和文件夹的权限、硬链接数、所有者、所有组、大小、最后修改时间和名称
        print(f"{permissions:4o} {hard_links:>5} {owner:<1} {group:<1} {size:>10} {mtime:<20} {filename}")

# 调用函数，列出当前目录下的所有文件和文件夹
list_directory(".")
# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

import os
# 定义一个函数，用于在指定目录及其子目录中查找包含特定字符串的文件
def find_files_with_string(root_dir, search_str):
    for dirpath, _, filenames in os.walk(root_dir):  # 使用os.walk()遍历指定目录及其子目录
        for filename in filenames:  # 遍历每个文件
            if search_str in filename:  # 如果文件名中包含搜索字符串
                print(os.path.relpath(os.path.join(dirpath, filename), root_dir))  # 打印文件相对于根目录的相对路径

# 调用函数
search_string = 'e'  # 替换为你要查找的字符串
find_files_with_string('.', search_string)  # 在当前目录中查找包含字符串'e'的文件
