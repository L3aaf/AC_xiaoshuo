# _*_coding:utf-8
# @Time      :2023/11/23 9:17
# @Author    :DQ
# @FileName: isTureF.py
import os
import re


class Tf:
    def __init__(self):
        # 初始化对象，设置初始目录为空，HTML路径默认为该目录
        self.dir = ''
        self.html_path = f'C:/Users/86132/PycharmProjects/pythonProject/Acxiaoshuo/download/html/{self.dir}'

    def set_dir(self, dir):
        # 设置目录的方法，同时更新HTML路径
        self.dir = dir
        self.html_path = f'C:/Users/86132/PycharmProjects/pythonProject/Acxiaoshuo/download/html/{self.dir}'

    def get_path_name(self):
        # 获取指定目录下的所有文件名的方法
        file_list = os.listdir(self.html_path)
        list_r = []
        for file in file_list:
            if os.path.isfile(os.path.join(self.html_path, file)):
                list_r.append(file)
        return list_r

    def get_title(self):
        # 从文件名中提取并返回不带扩展名的标题的方法
        file_list = self.get_path_name()
        pattern = r'(.*?).html'

        title_list = []

        if list:
            for file in file_list:
                match = re.search(pattern, file)
                if match:
                    title = match.group(1)
                    title_list.append(title)

        return title_list

    def search_title(self, title):
        # 搜索指定标题是否存在于文件名列表中的方法
        title_list = self.get_title()
        return title in title_list
